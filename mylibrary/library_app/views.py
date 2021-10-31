from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from .models import Book

# Create your views here.
from django.http import HttpResponse

#Function to add books and show them
def add_show_books(request):
    if request.method =='POST':
        fm = BookForm(request.POST)
        if fm.is_valid():
            isbn = fm.cleaned_data['isbn']
            title = fm.cleaned_data['title']
            author = fm.cleaned_data['author']
            add_date = fm.cleaned_data['add_date']
            reg = Book(isbn=isbn,title=title,author=author,add_date=add_date)
            reg.save()
            fm = BookForm()


    else:
        fm = BookForm()
    book_all=Book.objects.all()

    return render(request,'library_app/addandshow.html',{'form':fm,'boo':book_all})

#Function to uodate/delete books
def update_book(request,isbn):
    if request.method=='POST':
        pi = Book.objects.get(pk=isbn)
        fm = BookForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Book.objects.get(pk=isbn)
        fm = BookForm(instance=pi)

    return  render(request,'library_app/updatebook.html',{'form':fm})

# Function to delete books
def delete_book(request,isbn):
    if request.method=='POST':
        pi = Book.objects.get(pk=isbn)
        pi.delete()
        return HttpResponseRedirect('/library_app')

