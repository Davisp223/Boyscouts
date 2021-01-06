from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.


@login_required
def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'main/main.html', context)

