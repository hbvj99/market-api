from market.commons.searializers import DynamicFieldsModelSerializer
from market.notifications.models import Notification


class NotificationSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'description', 'is_seen', 'entity_type', 'created_at']
        read_only_fields = ('id',)
