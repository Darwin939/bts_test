from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    pages = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    tags = models.JSONField(default=list)

    def __str__(self):
        return self.title
