# import jwt
# from cuser.middleware import CuserMiddleware
# from rest_framework import exceptions
# from rest_framework.authentication import TokenAuthentication
#
# from config import settings
# from .models import AuthToken
#
#
# class CustomTokenAuthentication(TokenAuthentication):
#     model = AuthToken
#
#     def authenticate_credentials(self, key):
#         user, token = super().authenticate_credentials(key)
#
#         try:
#             jwt.decode(key, settings.SECRET_KEY, algorithms=['HS256'])
#         except (jwt.DecodeError, jwt.ExpiredSignatureError):
#             try:
#                 jwt.decode(token.refresh_token, settings.SECRET_KEY, algorithms=['HS256'])
#             except (jwt.DecodeError, jwt.ExpiredSignatureError):
#                 AuthToken.objects.get(key=key).delete()
#             raise exceptions.AuthenticationFailed('Invalid token')
#
#         CuserMiddleware.set_user(user)
#
#         return user, token
