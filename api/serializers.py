from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source = "poster.username")
    all_votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields =  ["id", "title", "url", "poster", "createdon", "all_votes"]

    def get_all_votes(self, obj):
        return Vote.objects.filter(post=obj).count()


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["id"]