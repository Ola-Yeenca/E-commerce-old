from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/set_sold/', views.set_sold, name='set_sold'),
    path('item/category/<int:pk>/', views.category, name='category'),
    # path('item/category/new_in/', views.category, name='new_in'),
]
