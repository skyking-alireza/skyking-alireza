from rest_framework.serializers import ModelSerializer
from .models import BlogModel , BlogCommentModel


class BlogSerializers(ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'
    
class BlogListSerializers(ModelSerializer):
    class Meta:
        model = BlogModel
        exclude = ['body',]

class BlogCommentSerializers(ModelSerializer):
    class Meta:
        model = BlogCommentModel
        fields = '__all__'