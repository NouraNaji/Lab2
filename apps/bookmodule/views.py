from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook1(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def about_us(request):
    return render(request, 'bookmodule/aboutus.html')