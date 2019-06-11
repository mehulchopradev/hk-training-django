from django.contrib import admin
from .models import Book, PublicationHouse, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'pages', 'price')
    search_fields = ('title',)
    list_filter = ('price', 'pages')
    fields = ('title', 'no_of_copies', 'pages', 'price', 'publication', 'pub_date')
    inlines = (ReviewInline,)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(PublicationHouse)
