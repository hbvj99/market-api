from ....models import Comment
from .....commons.searializers import DynamicFieldsModelSerializer


class CommentSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
