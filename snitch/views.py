from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()     #will hash the password fro security
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# @login_required
def home(request):
    user= request.user
    # profile = Profile.objects.filter(user=user.id)
    return render(request, 'home.html',{'user':user,'profile':profile})

def profile(request,id):
    user = request.user
    student = Student.objects.get(user=id)
    teacher = Teacher.objects.filter(pupil=user.id)
    context ={
        "student":student,'teacher':teacher
    }
    return render(request, 'profile.html',context)

def enter_teacher(request):
    user = request.user
    student = Student.objects.get(user=user)

    if request.method == 'POST':
        teacherform= TeacherDetailsForm(request.POST)
        if teacherform.is_valid():
            tform = teacherform.save(commit=False)
            tform.pupil= user
            tform.save()
        return redirect('profile', student.id)
    else:
        teacherform= TeacherDetailsForm()
    return render(request, 'enter_teacher.html',{'teacherform':teacherform})