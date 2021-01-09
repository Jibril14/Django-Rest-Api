from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = "poster.username")
    class Meta:
        model = Post
        fields =  ["id", "title", "url", "poster", "createdon" ]


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id"]