from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Student
from django.conf import settings
import csv

def show_landing(request):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:home'))

    username = request.session['username']
    books = Book.objects.all()
    context_data = {
        'books': books,
        'username': username
    }

    return render(request, 'libapp/private/landing.html', context_data)

def book_details(request, bookid):
    if 'username' not in request.session:
        return HttpResponseRedirect(reverse('library:home'))

    username = request.session['username']
    book = Book.objects.get(id=bookid)
    context_data = {
        'book': book,
        'username': username
    }

    return render(request, 'libapp/private/book_details.html', context_data)

def get_profile_pic(request):
    student_id = request.session['id']
    student = Student.objects.get(pk=student_id)
    path = student.profile_path
    if not path:
        path = 'no-image.png'
    final_path = '{0}{1}'.format(settings.MEDIA_ROOT, path)

    with open(final_path, mode='rb') as fp:
        return HttpResponse(fp.read(), content_type='image/*')
    

def logout(request):
    request.session.flush()
    return HttpResponseRedirect(reverse('library:home'))

def download_books(request):
    books = Book.objects.order_by('-price')
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    for book in books:
        writer.writerow([book.id, book.title, book.price, book.pages, book.publication.name])
    
    return response
