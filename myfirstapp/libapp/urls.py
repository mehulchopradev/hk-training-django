from django.urls import path
from .views import home, aboutus, contactus, showsignup, register, authenticate
from .authuserviews import show_landing, book_details, logout, get_profile_pic, download_books
from .rest_views import PublicationList, GetPublication

# to resolve url conflicts that can happen amongst various apps in the project
app_name = 'library'

# libmgmt/
urlpatterns = [
    path('home/', home, name='home'),
    path('about-us/', aboutus),
    path('contact/', contactus, name='contactus'),
    path('new-user/', showsignup, name='signup'),
    path('register/', register, name='register'),
    path('auth/', authenticate, name='auth'),
    path('landing/', show_landing, name='landing'),
    path('book-details/<int:bookid>', book_details, name='bookdetails'),
    path('logout/', logout, name='logout'),
    path('profilepic/', get_profile_pic, name='profilepic'),
    path('download-books/', download_books, name='downloadbooks'),

    path('api/publication-houses', PublicationList.as_view()),
    path('api/publication-houses/<int:pk>', GetPublication.as_view())
]