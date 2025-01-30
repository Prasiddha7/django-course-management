from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
import string


# Create your models here.

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def create_student(cls, name, email):
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        user = User.objects.create_user(username=email, email=email, password=password)
        student = cls(user=user, name=name)
        student.save()

        # Send password via email
        send_mail(
            'Your Course Management System Password',
            f'Hello {name},\nYour password is: {password}',
            'no-reply@yourdomain.com',
            [email],
            fail_silently=False,
        )
        return student