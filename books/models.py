from django.db import models

class Author(models.Model):
    author = models.CharField(max_length=256)

    def __str__(self):
        return self.author

class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'author')