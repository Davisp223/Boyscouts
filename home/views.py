from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

news = [
    {
        'date': '1/6/2021',
        'title': 'New Campouts',
        'body': 'There will be a new campout next month'
    }
]

def home(request):
    context = {
        'news': news
    }
    return render(request, 'home/home.html', context)

def recap(request):
    return render(request, 'home/recap.html')
