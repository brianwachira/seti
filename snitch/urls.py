from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('register/',views.register, name='register'),
    path('home/', views.home, name='home'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('enter-teacher', views.enter_teacher, name='enter_teacher')
    path('rate-teacher', views.rate_teacher)
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)