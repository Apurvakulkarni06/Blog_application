from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

from .models import Post
# Create your views here.

def index(request):
    post = Post.objects.all()

    context = {
        'title':'These are the Latest Posts',
        'post': post,
        }
    return render(request,'blog/index.html', context)

def details(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
        }
    

    return render(request,'blog/details.html', context)

def form(request):
    context = {
        'title':'Form',
    }
    return render(request,'blog/form.html', context) 
'''
def post_new(request):
    form = PostForm()
    return render(request, 'blog/edit.html', {'form': form})
   '''


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form': form})


