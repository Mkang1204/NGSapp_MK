## 20181120 MK fixed eror - 404 not find admin page -
# added import include and path to admin


from django.urls import path, include
from django.contrib import admin 

from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    # path(r'^login/$', auth_views.login, name='login'),
    # path(r'^logout/$', auth_views.logout, name='logout'),
    path('', views.home, name = 'home'),
    path('admin/', admin.site.urls),

    path('home/', views.home, name='home'),
    path('login/', auth_views.login, name = 'login'),
    path('logout/', auth_views.logout, name =  'logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')), #new

]