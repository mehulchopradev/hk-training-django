from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .models import Student
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'libapp/public/home.html')

def aboutus(request):
    pass

def contactus(request):
    # code written to get the phone and email from the database or some other service
    phone = '87678678768'
    email = 'contactus@lingnan.org.hk'

    context_data = {
        'phone': phone,
        'email': email
    }

    return render(request, 'libapp/public/contacts-us.html', context_data)

def showsignup(request):
    return render(request, 'libapp/public/signup.html')

def register(request):
    data = request.POST # has the incoming parameters with its values
    username, password, gender, country = data['username'], data['password'], data['gender'], data['country']

    filename = None

    if request.FILES and request.FILES['profile']:
        profile_file = request.FILES['profile']

        fs = FileSystemStorage()
        filename = fs.save('{0}/{1}'.format(username, profile_file.name), profile_file)

    # print(username, password, gender, country)
    s = Student(username=username, password=password, gender=gender, country=country,\
        profile_path=filename)

    try:
        s.save()
    except Exception:
        return HttpResponse('Server down. Please try later')
    else:
        return HttpResponseRedirect(reverse('library:home'))

def authenticate(request):
    data = request.POST
    username, password = data['username'], data['password']
    student_list = Student.objects.filter(username=username, password=password)
    if student_list:
        student = student_list[0]
        request.session['username'] = username
        request.session['id'] = student.id

        return HttpResponseRedirect(reverse('library:landing'))
    else:
        return HttpResponseRedirect(reverse('library:home'))