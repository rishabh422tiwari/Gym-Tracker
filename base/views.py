from django.shortcuts import render
from django.http import HttpResponse
from .models import Exercise

# Create your views here.
def say_hello(request):
    queryset = Exercise.objects.all()
    return render(request,'hello.html', {'name': 'rishabh'})