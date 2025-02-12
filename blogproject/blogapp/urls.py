from django.urls import path
from .views import blog_home, blog_detail, create_post, edit_post, delete_post, register, login_user, logout_user

urlpatterns = [
    path('', blog_home, name='blog-home'),
    path('post/<int:post_id>/', blog_detail, name='blog-detail'),
    path('create/', create_post, name='create-post'),
    path('post/<int:post_id>/edit/', edit_post, name='edit-post'),
    path('post/<int:post_id>/delete/', delete_post , name='delete-post'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
