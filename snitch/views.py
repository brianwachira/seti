from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import *

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

def home(request):
    user= request.user
    # profiles = Profile.objects.all()
    return render(request, 'home.html',{'user':user})