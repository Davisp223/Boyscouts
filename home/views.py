from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

emails = [
    {
        'author': 'Davis Plude',
        'date': '1/7/2021',
        'title': 'New Campout!!!',
        'content': 'There will be a new campout next month'
    }
]

def home(request):
    context = {
        'emails': emails
    }
    return render(request, 'home/home.html', context)

def recap(request):
    return render(request, 'home/recap.html')
