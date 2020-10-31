from django.contrib.auth import get_user_model
from rest_framework import serializers

from ....models import Product
from .....commons.searializers import DynamicFieldsModelSerializer
from .....users.api.v1.serializers import UserSerializer

User = get_user_model()


class ProductSerializer(DynamicFieldsModelSerializer):
    votes = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all().values_list('id', flat=True)),
        write_only=True)

    votes_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'product_id', 'title', 'slug', 'description', 'image', 'category', 'tags', 'votes', 'views',
                  'user', 'votes_count']
        read_only_fields = ('id', 'product_id', 'slug',
                            'votes', 'views', 'created_at', 'updated_at', 'deleted_at', 'votes_count')

    def get_votes_count(self, obj):
        return obj.votes.count()

    def get_fields(self):
        fields = super().get_fields()
        request = self.request
        if request and request.method.lower() == 'get':
            fields['user'] = UserSerializer(fields=('id', 'email ', 'first_name', 'last_name', 'image'))
            fields['votes'] = UserSerializer(fields=('id', 'first_name'), many=True)
        return fields
