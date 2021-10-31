from django.urls import path

from . import views

urlpatterns = [
    path('', views.add_show_books, name='AddandShow'),
    path('delete/<int:isbn>/', views.delete_book, name='delete_book'),
    path('update/<int:isbn>/', views.update_book, name='update_book'),

]