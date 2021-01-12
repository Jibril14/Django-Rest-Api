
from django.urls import path
from . import views
urlpatterns = [
 
    path('all-posts/', views.postlist.as_view(), name="postlist" ),
    path('vote/post/<int:pk>/', views.VoteCreate.as_view(), name="post-vote" ),
    path('post/<int:pk>/', views.PostRetrieveDestroy.as_view(), name="post-retrieve-destroy" ),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name="post-update" ),
    path('user/register/', views.signUpView, name="user-register" ),
    

]