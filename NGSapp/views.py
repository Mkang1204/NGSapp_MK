from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Run
from django.http import HttpResponse

from NGSapp.forms import HomeForm
 
# Create your views here.
def home(request):
    return render(request, 'home.html',{})


