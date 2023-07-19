from django.contrib import admin
from django.urls import include, path
from . import views

app_name = 'communication'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new'),
]
