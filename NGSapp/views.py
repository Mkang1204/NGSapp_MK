from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Run
from django.http import HttpResponse

from NGSapp.forms import HomeForm
 
# Create your views here.
def home(request):
    return render(request, 'home.html',{})

def result_view(request):
    # if request.method == 'GET'
    #     form = HomeForm(request.GET)
    #     if form.is_valid:
    #         run =

    #         return redirect('home')
    # else
    #     form = PostForm()

    data = Run.objects.all()
    runs = {
        'run_':data
    }
    return render(request, 'NGSapp/result_view.html',{'runs':runs})


def search_by_date(request):
    return render(request, 'search_by_date.html', {})

def search_by_pi(request):
    return render(request, 'search_by_pi.html', {})

def search_by_runid(request):
    return render(request, 'search_by_runid.html', {})