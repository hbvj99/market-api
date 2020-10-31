from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from market.commons.searializers import DynamicFieldsModelSerializer

User = get_user_model()


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'date_joined', 'email', 'bio', 'image']
        extra_kwargs = {
            'password': {
                'write_only': 'True'
            }
        }


class RegisterUserSerializer(DynamicFieldsModelSerializer):
    image = serializers.ImageField(default=None)
    confirm_password = serializers.CharField(max_length=100, allow_blank=False, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'confirm_password', 'image']
        extra_kwargs = {
            'password': {
                'write_only': 'True'
            }
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords didn't match.")

        import re
        if not re.match(r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#$%^&*()_+=\\<>?,./-]).{6,}$",
                        data['password']):
            raise serializers.ValidationError(
                "Password must contain at least 6 characters with one number and one special character.")
        return data

    def create(self, validated_data):
        _ = validated_data.pop('confirm_password')
        password = validated_data.pop('password')

        instance = super().create(validated_data)
        instance.is_active = False
        instance.set_password(password)
        instance.save()

        if validated_data:
            current_site = get_current_site(request=self.request)
            mail_subject = 'Activate your new account'
            message = render_to_string('email/register_email.html', {
                'user': instance,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
                'token': default_token_generator.make_token(instance),
            })
            to_email = validated_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

        return instance


class ResetPasswordSerializer(DynamicFieldsModelSerializer):
    old_password = serializers.CharField(max_length=80, write_only=True, required=True)
    new_password = serializers.CharField(max_length=90, required=True)
    confirm_password = serializers.CharField(max_length=90, required=True)

    def validate_old_password(self, value):
        instance = self.request.user
        if not instance.check_password(value):
            raise serializers.ValidationError("your old password didn't match.")
        return value

    def validate(self, data):
        if not data['new_password'] == data['confirm_password']:
            raise serializers.ValidationError("passwords didn't match.")

        import re
        if not re.match(r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[!@#$%^&()*_+=\\<>?,./-]).{6,}$",
                        data['new_password']):
            raise serializers.ValidationError(
                "password must contain at least 6 characters with one number and one special character.")

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ['old_password', 'new_password', 'confirm_password']
