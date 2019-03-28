from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length =50)
    PROGRAM_CHOICES = (
        ('Android','Android'),
        ('Python','Python')
    )
    program = models.CharField(max_length =50, choices=PROGRAM_CHOICES)
    pupil = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Teacher {self.name}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    PROGRAM_CHOICES = (
        ('Android','Android'),
        ('Python','Python')
    )
    program = models.CharField(max_length =50, choices=PROGRAM_CHOICES)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Student {self.user.username}"
