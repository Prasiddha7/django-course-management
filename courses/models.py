from django.db import models

# Create your models here.
class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Video', 'Video'),
        ('Document', 'Document'),
        ('MCQ', 'MCQ Quiz'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title