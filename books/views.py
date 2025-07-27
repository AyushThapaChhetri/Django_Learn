from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from books.forms import BookForm
from books.models import Book



# Create your views here.
def hello(request):
    return render(request, 'hello.html',{'name': 'Ayush'})
    # return render(request, 'hello.html')
    # return HttpResponse("Hello, %s!" % request.path)

# List all books (Read)
class BookListView(View):
   def get(self, request):
       books = Book.objects.all()
       return render(request, 'book_list.html', {'books': books})

# Create a book
class BookCreateView(View):
    def get(self, request):
        form = BookForm()
        return render(request, 'book_form.html', {'form': form})

    def post(self,request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'book_form.html', {'form': form})

#Update a book
class BookUpdateView(View):
    def get(self,request,uuid):
        book = get_object_or_404(Book, uuid=uuid)
        form = BookForm(instance=book)
        return render(request, 'book_form.html', {'form': form})

    def post(self,request,uuid):
        book = get_object_or_404(Book, uuid=uuid)
        form = BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        return render(request, 'book_form.html',{'form':form})

#Delete a book
class BookDeleteView(View):
    def get(self, request,uuid):
        book = get_object_or_404(Book, uuid=uuid)
        return render(request,'book_confirm_delete.html',{'book':book})

    def post(self,request,uuid):
        book = get_object_or_404(Book, uuid=uuid)
        book.delete()
        return redirect('book_list')

