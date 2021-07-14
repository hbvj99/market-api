from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from market.commons.paginations import StandardResultsSetPagination
from market.commons.viewsets import ListRetrieveViewSetMixin
from market.notifications.api.v1.serializers import NotificationSerializer
from market.notifications.models import Notification

User = get_user_model()


class NotificationViewSet(ListRetrieveViewSetMixin):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    pagination_class = StandardResultsSetPagination

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    filterset_fields = {
        'id': ['exact'],
        'entity_type': ['exact', 'in'],
        'created_at': ['gte', 'lte', 'exact', 'gt', 'lt'],
        'user': ['in', 'exact'],
        'is_seen': ['exact']
    }
    ordering_fields = ('id', 'entity_type', 'created_at', 'user')
    search_fields = ('description', 'entity_type', 'user__first_name')

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id).order_by('is_seen', '-updated_at')
