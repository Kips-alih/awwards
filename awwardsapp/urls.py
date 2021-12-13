from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^new/project$', views.new_project, name='newProject'),
    url('search/', views.search, name='search_results'),
]