from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', CharactersHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('cats/<int:catid>/', cat),
    path('history/', history),
    path('geography/', geography),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive),
    path('addpage', AddPage.as_view(), name='add_page'),
    path('feedback', feedback, name='feedback'),
    path('login', LoginUser.as_view(), name='login'),
    path('logout', logout_user, name='logout'),
    path('register', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CharactersCategory.as_view(), name='category')
]
