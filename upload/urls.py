from os import name
from django.urls import path
from . import views

app_name = 'upload'

urlpatterns = [

    path('upload/',views.index,name='uploads'),
    path('',views.login),
    path('search',views.search, name='search'),
    path('list',views.list)
    # path('json',views.json)
]
