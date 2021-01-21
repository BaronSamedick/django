from rest_framework.serializers import ModelSerializer

from main_app.models import Post


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
