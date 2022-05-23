from rest_framework import serializers
from blog.models import Post


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    text = serializers.CharField()
    created_date = serializers.DateTimeField()
    published_date = serializers.DateTimeField()


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
