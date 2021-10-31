from django.db import models

# Create your models here.
class Book(models.Model):
    isbn=models.CharField(max_length=13,primary_key=True)
    title=models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    add_date=models.DateField()
