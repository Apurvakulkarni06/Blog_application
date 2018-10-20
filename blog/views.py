from django.shortcuts import  render, redirect
from django.shortcuts import  get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from .forms import SignUpForm
from .forms import PostForm

from .models import Post

  #List of all the Post 
def index(request):
    post = Post.objects.all()

    context = {
        'title':'These are the Latest Posts',
        'post': post,
        }
    return render(request,'blog/index.html', context)
 #Posts detail page
def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
        }
    return render(request,'blog/details.html', context)
'''
def form(request):
    context = {
        'title':'Form',
    }
    return render(request,'blog/form.html', context) 
'''
 # signup page for user
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('blog:index')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})

# add the new post
def post_new(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('blog:details', id=post.id)
    else:
        form = PostForm()
    return render(request, 'blog/edit.html', {'form': form})    
   
def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('blog:details', id=post.id) 
    else:
        form = PostForm(instance = post)
    return render(request, 'blog/edit.html', {'form': form})          

