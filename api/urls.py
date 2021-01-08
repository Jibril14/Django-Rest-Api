
from django.urls import path
from . import views
urlpatterns = [
 
    path('all-posts', views.postlist.as_view(), name="postlist" ),
]