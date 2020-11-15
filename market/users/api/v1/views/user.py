from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import force_text
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

    @action(detail=False, url_path='verify-email', permission_classes=[AllowAny])
    def verify_email_token(self, request):
        uid = request.GET.get('uid')
        token = request.GET.get('token')
        if not (token and uid):
            raise exceptions.PermissionDenied("Token and uid is required.")
        try:
            uid = force_text(urlsafe_base64_decode(uid))
            user = self.get_queryset().get(pk=uid)
        except (ObjectDoesNotExist, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            if user.is_active is True:
                raise exceptions.NotAcceptable("email is already verified.")
            user.is_active = True
            user.save()
        else:
            raise exceptions.ValidationError("Token invalid or expired")
        serializer = self.get_serializer(user)
        return Response({'message': 'email has been verified', 'user info': serializer.data})


@action(methods=['post'], detail=False, url_path='password-change', serializer_class=ResetPasswordSerializer,
        permission_classes=[IsUserOwnerPermission])
def password_change(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    request.user.set_password(serializer.validated_data.get('new_password'))
    request.user.save()
    return Response({"message": "password has been reset with the new password."})
