from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        ordering = ["name", "date"]
        db_table = "Book"

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name", "age", "book"]
        db_table = "Customer"

    def __str__(self):
        return self.name
