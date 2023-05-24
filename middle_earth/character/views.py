import re
from typing import Any, Dict, List
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


from .forms import *
from .models import *
from .utils import *

# Create your views here.

#menu = {"About website", "New article", "Feedback", "Login"}
#menu = [{'title': "About website", 'url_name': 'about'},
#        {'title': "Create new page", 'url_name': 'add_page'},
#        {'title': "Feedback", 'url_name': 'feedback'},
#        {'title': "Log in", 'url_name': 'login'}]


class CharactersHome(DataMixin, ListView):
    model = Characters
    template_name: str = 'character/index.html'
    context_object_name = 'posts'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        context.update(c_def)
        return context

    def get_queryset(self):
        return Characters.objects.filter(is_published=True).select_related('cat')

# def index(request):
#     posts = Characters.objects.all()
#     #cats = Category.objects.all()

#     context = {
#         'posts': posts,
#         'title': 'Главная страница приложения character',
#         'cat_selected': 0
#         }
#     return render(request, 'character/index.html', context=context)

def about(request):
    return render(request, 'character/about.html', {'title': 'About site'})

def cat(request, catid):
    if (request.GET):
        print(request.GET)
    if (request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def history(request):
    return HttpResponse('<h2>История Средиземья</h2>')

def geography(request):
    return HttpResponse('<h2>Geography</h2>')

def archive(request, year):
    if int(year) > 2021:
        raise Http404()
    if int(year) < 1900:
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'character/addpage.html'
    success_url = reverse_lazy('home')

    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Add page")
        context.update(c_def)
        return context

# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             #Characters.objects.create(**form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'character/addpage.html', {'form': form, 'title': 'Добавление статьи'})

def feedback(request):
    return HttpResponse("Feedback")

# def login(request):
#     return HttpResponse("LOGIN")

class ShowPost(DataMixin, DetailView):
    model = Characters
    template_name = 'character/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="post")
        context.update(c_def)
        return context


# def show_post(request, post_slug):
#     #return HttpResponse(f'Article with id = {post_id}')
#     post = get_object_or_404(Characters, slug=post_slug)
#     print('test',post, 'end test')
#     print(post.photo)
#     context = {
#         'post': post,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }

#     return render(request, 'character/post.html', context=context)

class CharactersCategory(DataMixin, ListView):
    model = Characters
    template_name = 'character/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Category - ' + str(c.name), cat_selected=c.pk)
        context.update(c_def)
        return context

    def get_queryset(self):
        return Characters.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

# def show_category(request, cat_slug):
#     ccat_id = get_object_or_404(Category, slug=cat_slug).id
#     posts = Characters.objects.filter(cat_id=ccat_id)
#     print(cat_slug)
#     print(posts)
#     #cats = Category.objects.all()
#     if len(posts) == 0:
#         raise Http404()

#     context = {
#         'posts': posts,
#         'title': 'Отображение по рубрикам',
#         #'cat_selected': posts[0].cat_id
#         'cat_selected': ccat_id
#         }
#     return render(request, 'character/index.html', context=context)

class RegisterUser(DataMixin, CreateView):
    #form_class = UserCreationForm
    form_class = RegisterUserForm
    template_name = 'character/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Register')
        context.update(c_def)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'character/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        context.update(c_def)
        return context  

    def get_success_url(self) -> str:
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')
