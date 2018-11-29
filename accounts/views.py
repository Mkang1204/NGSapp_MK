from django.contrib.auth.forms import *
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
    return render(request, 'accounts/signup.html', context)

def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/view_profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


def reset_password(request):
    return render(request, 'accounts/reset_password.html', args)