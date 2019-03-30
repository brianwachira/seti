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

    def save_teacher(self):
        self.save()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField( upload_to='profile_pics', default='default.jpeg',)

    def __str__(self):
        return f"Student {self.user.username}"

    def save_student(self):
        self.save()

class Rate(models.Model):
    stud = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    scale = models.IntegerField(default=0)

    def save_rate(self):
        self.save()


