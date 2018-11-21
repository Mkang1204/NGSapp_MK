from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from NGSapp.models import User
from django.shortcuts import render

# Create your views here.
class SignUp(generic.CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def queryset(request):
    return render(request, 'signup.html',{})


def model(request):
    return render(request,'signup.html', {})