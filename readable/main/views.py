from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from readable.helpers import lookup
from main.models import Book, ReadingStatus
from users.forms import ListUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages



@login_required
# home page
def home(request):
    return render(request, 'main/home.html')

# about the project page
def about(request):
    return render(request, 'main/about.html')

# library
@login_required
def library(request):
    if request.method == 'POST' and "search" in request.POST:
        result = lookup(request.POST.get('search'))
        forms = []
        for r in result:
            form = ListUpdateForm(initial={
            "title": r["title"],
            "google_id": r["id"],
            "description": r["description"],
            "authors" : r["authors"],
            "cover_url" : r["cover_url"]
            })
            forms.append(form)

        context = {
            'results' : zip(result, forms)
        }
        return render(request, 'main/library.html', context)

    else:
        return render(request, 'main/library.html')

@login_required
def reading_status(request):
    if request.method == "POST":
        # other forms - putting books into private collections
        form_list_type = ListUpdateForm(request.POST)

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
                    title=request.POST["title"]
            )
            b.save()
        
        #form_list_type.fields["user"] = u
        #form_list_type.fields["book"] = b
        # book there or created, put the data to database            
        #if form_list_type.is_valid():
        #    form_list_type.save()
        #    messages.success(request, f'The book has been added to your collection!')



        # metoda 2: po walidacji reczne utworzenie relacji
        if form_list_type.is_valid():
            reading_status = form_list_type.save(commit=False)
            reading_status.book = b
            reading_status.user = u
            reading_status.save()
            messages.success(request, f'The book has been added to your collection!')
    return redirect("main-library")