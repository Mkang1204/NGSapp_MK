from django.urls import path
from . import views

urlpatterns = [
    # path('signup/', views.SignUp.as_view()),
    path('signup/', views.signup, name = 'signup'),
    path('view_profile/', views.view_profile, name = 'profile'),
    path('profile/edit/', views.edit_profile, name = 'edit_profile'),
    path('change_password/', views.change_password, name = 'change_password'),
    path('reset_password/', views.reset_password, name = 'reset_password')
]