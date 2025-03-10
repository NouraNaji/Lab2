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

def html5_links(request):
    return render(request, 'bookmodule/html5_links.html') 

def text_formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing_page(request):
    return render(request, 'bookmodule/listing.html')

def tables_page(request):
    return render(request, 'bookmodule/tables.html')









def search_books(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        is_title = request.POST.get('option1')  # البحث في العنوان
        is_author = request.POST.get('option2')  # البحث في المؤلف
        
        books = __getBooksList()
        filtered_books = []

        for book in books:
            found = False
            if is_title and keyword in book['title'].lower():
                found = True
            if not found and is_author and keyword in book['author'].lower():
                found = True

            if found:
                filtered_books.append(book)

        return render(request, 'bookmodule/bookList.html', {'books': filtered_books})

    return render(request, "bookmodule/search.html")

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]