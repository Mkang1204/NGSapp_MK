from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from NGSapp.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
# class SignUp(generic.CreateView):
#     from_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'

# def queryset(request):
#     return render(request, 'signup.html',{})


# def model(request):
#     return render(request,'signup.html', {})


def signup(request):
    '''Sign up a new user'''
    form = UserCreationForm()

    if form.is_valid():
        new_user = form.save()

        pw = request.POST['password1']
        authenticated_user = authenticated(username = new_user.username, password = pw)

        login(request, authenticated_user)
        return HttpResponseRedirect(
            reverse_lazy('login')
        )
    context = {'form':form}
    return render(request, '/signup.html', context)