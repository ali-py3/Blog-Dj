from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm


# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'title_tag', 'author', 'body')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'Update_post.html'
    form_class = EditForm
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'Delete_post.html'
    success_url = reverse_lazy('home')

