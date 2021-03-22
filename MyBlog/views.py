from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request,'home.html',{})

def LikeView(request, pk):
    post = get_object_or_404(Post,id = request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-view', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    name = Category.objects.all()
    ordering = ['-id']

    def get_context_data(self, *args, **kwargs):
        name_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["name_menu"] = name_menu
        return context


def CategoryListView(request):
    category_list_posts = Category.objects.all()
    return render(request, 'category_list.html',{'category_list_posts': category_list_posts})


def CategoryView(request, name):
    category_posts = Post.objects.filter(category=name.replace('-', ' '))
    return render(request, 'category.html', {'name': name.replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        name_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuf = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuf.total_likes()
        context["name_menu"] = name_menu
        context["total_likes"] = total_likes
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'title_tag', 'author', 'body')


class AddCategoryView(CreateView):
    model = Category

    template_name = 'add_category.html'
    fields = ('__all__')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'Update_post.html'
    form_class = EditForm
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'Delete_post.html'
    success_url = reverse_lazy('home')
