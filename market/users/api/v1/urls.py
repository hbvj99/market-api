from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import Register, UserViewSet

router = DefaultRouter()

router.register('', UserViewSet, 'users')

urlpatterns = [
                  path('register/', Register.as_view(), name='user-register'),
              ] + router.urls
