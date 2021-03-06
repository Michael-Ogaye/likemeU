from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('signup/', views.signup, name='signup'),
   
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
     path('like', views.like_post, name='like_post'),
    path('search/', views.search_profile, name='search'),
    path('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    path('follow/<to_follow>', views.follow, name='follow'),
    path('post/<id>', views.post_comment, name='comment'),
    path('post/<id>/like', views.PostLikeToggle.as_view(), name='liked'),
    path('api/post/<id>/like', views.PostLikeAPIToggle.as_view(), name='liked-api'),
    path('signout/',views.signout,name='signout')
]