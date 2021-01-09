from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = "poster.username")
    class Meta:
        model = Post
        fields =  ["id", "title", "url", "poster", "createdon" ]



