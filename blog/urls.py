from django.urls import path
from .views import PostListView,\
    AboutView, \
    PostDetailView, \
    PostCreateView,\
    PostUpdateView,\
    PostDeleteView,\
    UserPostListView,\
    LikeView


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', AboutView.as_view(), name='blog-about'),
    path('like/<int:pk>', LikeView.as_view(), name="like-post")
]


