from django.shortcuts import render

# Create your views here.
def run_list(request):
    return render(request, 'NGSapp/run_list.html',{})
