from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class TeacherDetailsForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','program']

class RateForm(forms.ModelForm):
    RATINGS= (
      (1,''),
      (2,''),
      (3,''),
      (4,''),
      (5,''),
      (6,''),
      (7,''),
      (8,''),
      (9,''),
      (10,'')
    )
    scale = forms.ChoiceField(choices=RATINGS, widget=forms.RadioSelect())
    class Meta:
        model = Rate
        exclude = ['stud','teacher']

# class FeedbackForm(forms.ModelForm):
#     class Meta:
#         model = Feedback
#         exclude = ['stud','teacher']
#         widgets = {
#             'opinion': forms.TextInput(attrs={'placeholder':'Add a feedback'})
#         }
