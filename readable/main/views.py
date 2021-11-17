from typing import Counter
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from readable.helpers import lookup
from main.models import Book, ReadingStatus
from users.forms import BookAddingForm, ListUpdateForm, ReadingProgress, ProgressUpdate
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone



@login_required
# home page
def home(request):
    # load current goal and count the read books in current year
    r = ReadingProgress.objects.get(user=request.user)
    goal = r.year_goal
    current_year = timezone.now().year
    q_set = ReadingStatus.objects.filter(user=request.user).filter(list_type="H")
    count = 0
    for q in q_set:
        if q.date_added.year == current_year:
            count += 1

    context = {
        'goal' : goal,
        'count' : count
    }
    return render(request, 'main/home.html', context)

# about the project page
def about(request):
    return render(request, 'main/about.html')

# library
@login_required
def library(request):
    # load current goal and count the read books in current year
    r = ReadingProgress.objects.get(user=request.user)
    goal = r.year_goal
    current_year = timezone.now().year
    q_set = ReadingStatus.objects.filter(user=request.user).filter(list_type="H")
    count = 0
    for q in q_set:
        if q.date_added.year == current_year:
            count += 1

    context = {
        'goal' : goal,
        'count' : count
    }

    if request.method == 'POST' and "search" in request.POST:
        result = lookup(request.POST.get('search'))
        forms = []
        for r in result:
            form = BookAddingForm(initial={
            "title": r["title"],
            "google_id": r["id"],
            "description": r["description"],
            "authors" : r["authors"],
            "cover_url" : r["cover_url"],
            "info_url" : r["info_url"]
            })
            forms.append(form)

        context = {
            'results' : zip(result, forms),
            'goal' : goal,
            'count' : count
        }
        return render(request, 'main/library.html', context)

    else:
        return render(request, 'main/library.html', context)

# Adding books to users collection
@login_required
def create_status(request):
    if request.method == "POST":
        form_list_type = BookAddingForm(request.POST)

        # currently logged in user
        u = User.objects.get(id=request.user.id)
        
        # check if this book is already in the database
        b = Book.objects.filter(google_id=request.POST["google_id"]).first()
        if not b:
            b = Book(
                    google_id=request.POST["google_id"], 
                    description=request.POST["description"], 
                    cover_url=request.POST["cover_url"], 
                    authors=request.POST["authors"],
                    title=request.POST["title"],
                    info_url=request.POST["info_url"]
            )
            b.save()
        
        if form_list_type.is_valid():
            reading_status = form_list_type.save(commit=False)
            reading_status.book = b
            reading_status.user = u
            reading_status.save()
            messages.success(request, f'The book has been added to your collection!')

    return redirect("main-library")



# Viewing collections
@login_required
def bookshelf(request):

    # load current goal and count the read books in current year
    r = ReadingProgress.objects.get(user=request.user)
    goal = r.year_goal
    current_year = timezone.now().year
    q_set = ReadingStatus.objects.filter(user=request.user).filter(list_type="H")
    count = 0
    for q in q_set:
        if q.date_added.year == current_year:
            count += 1

    # load all books from the current user
    search = ReadingStatus.objects.filter(user=request.user)
    to_read =[]
    reading = []
    have_read = []
    forms_t = []
    forms_r = []
    forms_h = []

    # creating all of the users book lists
    for r in search:
        if r.list_type == 'T':
            to_read.append(r)
            form = ListUpdateForm(instance=r)
            forms_t.append(form)
        if r.list_type == 'R':
            reading.append(r)
            form = ListUpdateForm(request.POST or None, instance=r)
            forms_r.append(form)
        if r.list_type == 'H':
            have_read.append(r)
            form = ListUpdateForm(request.POST or None, instance=r)
            forms_h.append(form)

    context = {
        'to_read' : list(zip(to_read, forms_t)),
        'reading' : list(zip(reading, forms_r)),
        'have_read' : list(zip(have_read, forms_h)),
        'goal' : goal,
        'count' : count
    }

    return render(request, 'main/bookshelf.html', context)



# Move the book to other collection
@login_required
def update_status(request, status_id):
    status = ReadingStatus.objects.get(pk=status_id)
    form = ListUpdateForm(request.POST or None, instance=status)   
    if form.is_valid():
        form.save()
        status = ReadingStatus.objects.get(pk=status_id)
        messages.success(request, f'The book "{status.book.title}" has been moved to "{status.get_list_type_display()}" collection!')   
        return redirect('main-bookshelf')



# Delete the book from the collections
@login_required
def delete_status(request, status_id):
    status = ReadingStatus.objects.get(pk=status_id)
    status.delete()
    messages.success(request, f'The book has been deleted from your collection!')   
    return redirect('main-bookshelf')


# Reccomendations
@login_required
def reco(request):
    # load current goal and count the read books in current year
    r = ReadingProgress.objects.get(user=request.user)
    goal = r.year_goal
    current_year = timezone.now().year
    q_set = ReadingStatus.objects.filter(user=request.user).filter(list_type="H")
    count = 0
    for q in q_set:
        if q.date_added.year == current_year:
            count += 1
    context = {
        'goal' : goal,
        'count' : count
    }
    return render(request, 'main/reco.html', context)    

# Reading progress
@login_required
def progress(request):

    # load current goal and count the read books in current year
    r = ReadingProgress.objects.get(user=request.user)
    goal = r.year_goal
    current_year = timezone.now().year
    q_set = ReadingStatus.objects.filter(user=request.user).filter(list_type="H")
    count = 0
    for q in q_set:
        if q.date_added.year == current_year:
            count += 1
    else:
        i = ReadingProgress.objects.filter(user=request.user).first()
        form = ProgressUpdate(instance=i)
        context = {
            "form" : form,
            'goal' : goal,
            'count' : count
        }
    return render(request, 'main/progress.html', context)

def progress_update(request):
    if request.method == "POST":
        form = ProgressUpdate(request.POST, instance=ReadingProgress.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            f = form.cleaned_data['year_goal']
            messages.success(request, f'Your yeraly goal has been changed to {f}!')   
            return redirect('main-progress')


def contact(request):
    return render(request, 'main/contact.html')