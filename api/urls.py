
from django.urls import path
from . import views
urlpatterns = [
 
    path('all-posts/', views.postlist.as_view(), name="postlist" ),
    path('vote/post/<int:pk>/', views.VoteCreate.as_view(), name="post-vote" ),
]