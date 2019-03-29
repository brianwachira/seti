from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth import login,authenticate

# Create your views here.
def register(request):
    if request.method == 'POST':
        userform = UserRegisterForm(request.POST)
        if userform.is_valid():
            userform.save()     #will save userif form is valid
            user = userform.save(commit=False)  #creatin a usre object from the form but it proevents the object from bein saved
            username = userform.cleaned_data.get('username')
            raw_password= userform.cleaned_data.get('password')
        
            student = Student(user=user)        #creating an instance of student with this user. The user in blue is foreign key of student, WE have to save an object to forin key, nt an id
            student.save()
            return redirect('login')
    else:
        userform = UserRegisterForm()
    return render(request, 'users/register.html', {'userform': userform})

# @login_required
def home(request):
    user= request.user
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
    if request.method == 'POST':
        teacherform= TeacherDetailsForm(request.POST)
        if teacherform.is_valid():
            tform = teacherform.save(commit=False)
            tform.pupil= user
            tform.save()
        return redirect('profile', user.id)
    else:
        teacherform= TeacherDetailsForm()
    return render(request, 'enter_teacher.html',{'teacherform':teacherform})

def rate_teacher(request,id):
    user=request.user
    teacher = Teacher.objects.get(id=id)
    rates = Rate.objects.filter(teacher=teacher).first()
    
    if request.method == 'POST':
        rform= RateForm(request.POST)
        if rform.is_valid() and rates is None:
            rate=rform.save(commit=False)
            rate.stud=user
            rate.teacher=teacher
            rate.save()
        return redirect('rate_teacher', teacher.id)
    else:
        rform=RateForm()
        all_rates = Rate.objects.filter(teacher=teacher)

    context ={
       'teacher':teacher, 'rform':rform, 'all_rates':all_rates
    }
    return render(request, 'evaluate.html',context)

# 
