from django.urls import path
from . import views
from .views import search_books
from .models import Book



urlpatterns = [
    path('', views.index, name='books.index'),
    path('list/', views.list_books, name='books.list_books'),
    path('book/<int:bookId>/', views.viewbook1, name='books.view_one_book'),
    path('about/', views.about_us, name='books.aboutus'),
    path('html5/links/', views.html5_links, name='html5_links'), 
    path('html5/text/formatting/', views.text_formatting, name='text_formatting'),
    path('html5/listing/', views.listing_page, name='html5_listing'),
    path('html5/tables/', views.tables_page, name='html5_tables'),
    path('books/search/', search_books, name='search_books'),
    path("add_books/", views.add_books, name="add_books"), 
    path("simple/query", views.simple_query, name="simple_query"),
    path("complex/query", views.complex_query, name="complex_query"),
    path('lab8/task1/', views.task1, name='task1'),  
    path('lab8/task2/', views.task2, name='task2'),  
    path('lab8/task3/', views.task3, name='task3'), 
    path('lab8/task4/', views.task4, name='task4'), 
    path('lab8/task5/', views.task5, name='task5'), 
    path('lab8/task7/', views.student_count_by_city, name='student_count'),
    path('lab8/add-students/', views.add_students, name='add_students'),
    path('lab9/task1/', views.task1_lab9, name='lab9-task1'),
    path('lab9/task2/', views.task2_lab9, name='lab9-task2'),
    path('lab9/task3/', views.task3_lab9, name='lab9-task3'),
    path('lab9/task4/', views.task4_lab9, name='lab9-task4'),
    # path('lab10_part1/listbooks/', views.list_books, name='list_books'),
    # path('lab10_part1/add_book/', views.add_book, name='add_book'),  
    # path('lab10_part1/editbook/<int:id>', views.edit_book, name='edit_book'),  
    # path('lab10_part1/deletebook/<int:id>/', views.delete_book, name='delete_book'),
    # path('lab10_part2/listbooks/', views.list_books, name='list_books_part2'),
    # path('lab10_part2/addbook/', views.add_book, name='add_book_part2'),
    # path('lab10_part2/editbook/<int:id>/', views.edit_book, name='edit_book_part2'),
    # path('lab10_part2/deletebook/<int:id>/', views.delete_book, name='delete_book_part2'),
    path('add-address/', views.add_address, name='add_address'),
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.student_add, name='student_add'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('add-address2/', views.add_address2, name='add_address2'),
    path('students2/', views.list_students2, name='list_students2'),
    path('students2/add/', views.add_student2, name='add_student2'),
    path('add-cover/', views.add_book_cover, name='add_book_cover'),
    path('covers/', views.list_book_covers, name='list_book_covers'),




]
