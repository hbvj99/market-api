from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from market.commons.viewsets import ListCreateRetrieveDestroyViewSetMixin
from ..serializers.comment import CommentSerializer
from .....commons.paginations import StandardResultsSetPagination
from .....products.models import Comment
from .....users.permissions import IsProductOwnerPermission


class CommentViewSet(ListCreateRetrieveDestroyViewSetMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsProductOwnerPermission]

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('id', 'created_at', 'updated_at')
