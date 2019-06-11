from django.db import models

# Create your models here.

class Student(models.Model):
    # id (default given by django model layer)
    username = models.CharField(null=False, max_length=20)
    password = models.CharField(null=False, max_length=20)
    gender = models.CharField(null=False, max_length=1)
    country = models.CharField(null=True, max_length=5)
    profile_path = models.CharField(null=True, max_length=100)

class PublicationHouse(models.Model):
    name = models.CharField(null=False, max_length=40)
    ratings = models.IntegerField(null=False)

    # One to many
    # book_set

    def __str__(self):
        return self.name

class Book(models.Model):
    # id
    title = models.CharField(null=False, max_length=50)
    price = models.FloatField(null=True)
    pages = models.IntegerField(null=False)
    no_of_copies = models.IntegerField(null=False)
    publication = models.ForeignKey(PublicationHouse, on_delete=models.CASCADE, default=None)
    pub_date = models.DateField(null=True)
    students = models.ManyToManyField(Student, through='BooksStudentsRel')

    # One to many (Review)
    # review_set

    def __str__(self):
        return self.title

class Review(models.Model):
    reviewer = models.CharField(null=False, max_length=20)
    description = models.CharField(null=False, max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

class BooksStudentsRel(models.Model):
    # id
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    issue_date = models.DateField(null=False)
    return_date = models.DateField(null=True)
