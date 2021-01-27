from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,  
)
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import Patch
from .models import Feedback

# Create your views here.

#other
@login_required
def soon(request):
    return render(request, 'main/soon.html',)

class ChangeLogView(LoginRequiredMixin, ListView):
    model = Patch
    template_name = 'main/changelog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Patchs'
    ordering = ['-date_posted']

#feedback

class FeedbackView(LoginRequiredMixin, ListView):
    model = Feedback
    template_name = 'main/feedback.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'Feedbacks'
    ordering = ['-date_posted']

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



#posts
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'main/main.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/main/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False







