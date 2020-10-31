from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.utils.http import urlsafe_base64_decode
from rest_framework import exceptions
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers import RegisterUserSerializer, UserSerializer, ResetPasswordSerializer
from ....permissions import IsAdminPermission, IsUserOwnerPermission
from .....commons.viewsets import ListRetrieveSetMixin

User = get_user_model()


class Register(CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']


class UserViewSet(ListRetrieveSetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminPermission]

    @action(methods=['post'], detail=False, url_path='verify-email')
    def verify_email_token(self, request, uidb64, token):
        token = request.data.get('token')

        if not token:
            raise exceptions.PermissionDenied("Token is required")

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.default_manager.get(pk=uid)
        except (ObjectDoesNotExist, ValueError, OverflowError, User.DoesNotExist):
            raise exceptions.ValidationError("Token invalid or expired")

        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    @action(methods=['post'], detail=False, url_path='password-change', serializer_class=ResetPasswordSerializer,
            permission_classes=[IsUserOwnerPermission])
    def password_change(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data.get('new_password'))
        request.user.save()
        return Response({"message": "password has been reset with the new password."})
