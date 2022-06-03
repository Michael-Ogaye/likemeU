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
    return render(request, 'registration/signup.html', {'form': form})


