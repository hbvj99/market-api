from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, CommentViewSet

router = DefaultRouter()

router.register('comments', CommentViewSet, 'comments')
router.register('', ProjectViewSet, 'products')

urlpatterns = [
              ] + router.urls
