from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

# Create your views here.


def home(request):
    context = {
        "posts": Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewType>.html
    context_object_name = 'posts'
    ordering = ['-date']

class PostDetailView(DetailView):
    model = Post
   
   
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   
  
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'context']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False 
   

def about(request):
    return render(request, 'blog/about.html', {"title": "About"})



