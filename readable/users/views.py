from django.contrib.messages.api import error
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from main.models import ReadingProgress

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account "{username}" has been created! You are able to log in now!')
            r = ReadingProgress(user=form.instance)
            r.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # load current goal and count the read books in current year
    r = ReadingProgress.objects.get(user=request.user)
    goal = r.year_goal
    current_year = timezone.now().year
    q_set = ReadingStatus.objects.filter(user=request.user).filter(list_type="H")
    count = 0
    for q in q_set:
        if q.date_added.year == current_year:
            count += 1
    



    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'goal' : goal,
        'count' : count
    }
    return render(request, 'users/profile.html', context)