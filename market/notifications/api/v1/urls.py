from rest_framework.routers import DefaultRouter

from market.notifications.api.v1.views import NotificationViewSet

router = DefaultRouter()

router.register('', NotificationViewSet, 'notifications')

urlpatterns = [] + router.urls
