from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Post, Comment, Profile, Follow
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
from .forms import RegForm,PostForm,UpdateUserProfileForm,UpdateUserForm,CommentForm




def signup(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            f_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=f_password)
            login(request, user)
            return redirect('index')
    else:
        form = RegForm()
    return render(request, 'reg/signup.html', {'form': form})



@login_required(login_url='login')
def index(request):
    images = Post.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    context = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'plata/index.html', context)
