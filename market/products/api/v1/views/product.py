from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import exceptions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .....commons.paginations import StandardResultsSetPagination
from .....commons.viewsets import ListCreateRetrieveDestroyViewSetMixin
from .....products.api.v1.serializers import ProductSerializer
from .....products.models.product import Product
from .....users.permissions import IsProductOwnerPermission, IsAuthenticatedOrReadOnly

User = get_user_model()


class ProjectViewSet(ListCreateRetrieveDestroyViewSetMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('user', 'title', 'description', 'category', 'tags')
    search_fields = ('title', 'description', 'category', 'tags')

    def get_permissions(self):
        permissions = []
        if self.action in ['destroy', 'update', 'partial_update']:
            permissions = [IsProductOwnerPermission]
        elif self.action in ['list', 'retrieve']:
            permissions = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permissions]

    @action(methods=['get'], detail=False, url_path='has-product', permission_classes=[IsAuthenticatedOrReadOnly])
    def active_listening(self, request):
        user_id = request.GET.get('client')
        if not user_id:
            raise exceptions.ValidationError("id is required")
        if not Product.objects.filter(id=user_id).exists():
            raise exceptions.ValidationError("you don't have active product for listening")
        total_product = Product.objects.exclude(id=None).count()
        return Response(f"you have {total_product} active product")
