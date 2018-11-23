from django.shortcuts import render, redirect, HttpResponse

from .models import TourismConfig

# Create your views here.

def index(request):
    books = TourismConfig.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)

def create(request):
    print(request.POST)
    title = request.GET['title']
    price = request.GET['price']
    author = request.GET['author']
    book_details = TourismConfig(title=title, price=price, author=author)
    book_details.save()
    return redirect('/')


def add_place(request):
    return render(request, 'add_place.html')



def delete(request, id):
    books = TourismConfig.objects.get(pk=id)
    books.delete()
    return redirect('/')

def edit(request, id):
    books = TourismConfig.objects.get(pk=id)
    context = {
        'books': books
    }
    return render(request, 'edit.html', context)


def update(request, id):
    books = TourismConfig.objects.get(pk=id)
    books.title = request.GET['title']
    books.price = request.GET['price']
    books.author = request.GET['author']
    books.save()
    return redirect('/')

