from rest_framework import serializers

from member.serializer import UserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = Post
        fields = ('id', 'author', 'photo', 'created_at')
        read_only_fields = ('author',)