from rest_framework.serializers import ModelSerializer
from .models import PageModel
class PageSerializer(ModelSerializer):
    class Meta:
        model = PageModel
        fields = '__all__'

class PageListSerializer(ModelSerializer):
    class Meta:
        model = PageModel
        exclude = ['body',]