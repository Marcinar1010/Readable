from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from readable.helpers import lookup


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
    if request.method == 'POST':
        form = request.POST.get('search')
        result = lookup(form)

        context = {
            'result' : result
        }
        return render(request, 'main/library.html', context)
    else:
        return render(request, 'main/library.html')
