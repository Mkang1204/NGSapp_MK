from django.shortcuts import render
from django.utils import timezone
from .models import Run
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',{})


