from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='books.index'),
    path('list/', views.list_books, name='books.list_books'),
    path('book/<int:bookId>/', views.viewbook1, name='books.view_one_book'),
    path('about/', views.about_us, name='books.aboutus'),
]