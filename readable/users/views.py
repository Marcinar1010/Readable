from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You now are able to log in!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')