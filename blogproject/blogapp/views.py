from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blogapp/home.html', {'posts': posts})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blogapp/blog_detail.html', {'post': post})


def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('blog-home')  

    else:
        form = BlogPostForm()  

    return render(request, 'blogapp/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-detail', post_id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogapp/edit_post.html', {'form':form, 'post':post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-home')
    return render(request, 'blogapp/post_delete.html', {'post': post})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('blog-home')
    else:
        form = RegisterForm()

    return render(request, 'blogapp/register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog-home')
    else: 
        form = AuthenticationForm()
    return render(request, 'blogapp/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')