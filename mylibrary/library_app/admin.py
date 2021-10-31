from django.contrib import admin
from  .models import Book

class QuestionAdmin(admin.ModelAdmin):
    fields = ['isbn', 'title','author','add_date']

admin.site.register(Book, QuestionAdmin)

# Register your models here.
