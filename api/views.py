from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

class postlist(generics.ListCreateAPIView):
   queryset = Post.objects.all()
   serializer_class = PostSerializer

   def perform_create(self, serializer):
      serializer.save(poster=self.request.user)

class VoteCreate(generics.CreateAPIView):
   serializer_class = VoteSerializer
   permission_classes = [permissions.IsAuthenticated]

   def get_queryset(self):
      user = self.request.user
      post = Post.objects.get(pk=self.kwargs["pk"])
      return Vote.objects.filter(voter=user, post=post)

   def perform_create(self, serializer):
      if self.get_queryset().exists():
         raise ValidationError("You Voted already")
      serializer.save(voter = self.request.user, post=Post.objects.get(pk=self.kwargs["pk"]))
