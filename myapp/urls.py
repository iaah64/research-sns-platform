from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'sns.html', views.sns, name='sns'),
    path(r'search.html', views.search, name='search'),
    path(r'profile.html', views.profile, name='profile'),
    path("ajax/", views.logging, name="logging"),
]
