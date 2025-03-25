from django.urls import path
from . import views
from .views import search_books

urlpatterns = [
    path('', views.index, name='books.index'),
    path('list/', views.list_books, name='books.list_books'),
    path('book/<int:bookId>/', views.viewbook1, name='books.view_one_book'),
    path('about/', views.about_us, name='books.aboutus'),
    path('about/', views.about_us, name='books.aboutus'),
    path('html5/links/', views.html5_links, name='html5_links'), 
    path('html5/text/formatting/', views.text_formatting, name='text_formatting'),
    path('html5/listing/', views.listing_page, name='html5_listing'),
    path('html5/tables/', views.tables_page, name='html5_tables'),
    path('books/search/', search_books, name='search_books'),  # Ensure the trailing slash
    path('html5/tables/', views.tables_page, name='html5_tables'),
    path("add_books/", views.add_books, name="add_books"), 
    path("simple/query", views.simple_query, name="simple_query"),
    path("complex/query", views.complex_query, name="complex_query"),

    

]