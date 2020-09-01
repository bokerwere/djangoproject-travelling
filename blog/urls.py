from django.urls import path
from .views import  PostListView, PostDetailView, PostCreatView,PostUpdateView,PostDeleteView,UserPostListView
from . import views
#instead of using views use PostListWiew/class base

urlpatterns = [

    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
  path('user/<str:username>/', UserPostListView.as_view(), name='user_post'),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
   path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
   path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
   path('post/new/', PostCreatView.as_view(), name='post_create'),
    path('about',views.about, name='blog-about')
]


