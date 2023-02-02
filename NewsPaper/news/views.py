from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.urls import reverse_lazy

class PostList(ListView):
    model = Post
    ordering = '-time'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10
    def get_queryset(self):
    # Получаем обычный запрос
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

class SearchPost(ListView):
    model = Post
    ordering = '-time'
    template_name = 'search_post.html'
    context_object_name = 'posts'
    paginate_by = 10
    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class NewsCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'
    def form_valid(self, form):
        post = form.save(commit=False)
        post.position = 'NEW'
        return super().form_valid(form)

class NewsUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('post_list')

class ArticlesCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

class ArticlesUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'articles_edit.html'

class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'articles_delete.html'
    success_url = reverse_lazy('post_list')
