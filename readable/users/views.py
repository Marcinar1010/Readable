from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can sign In now!')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})





def login(request):
    return render(request, 'users/login.html')

