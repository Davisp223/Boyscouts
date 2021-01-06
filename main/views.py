from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

emails = [
    {
        'author': 'Davis Plude',
        'date': '1/7/2021',
        'title': 'New Campout!!!',
        'content': 'There will be a new campout next month'
    }
]
@login_required
def main(request):
    context = {
        'emails': emails
    }
    return render(request, 'main/main.html', context)

