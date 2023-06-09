from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [

   # sessions
   path('login/', views.LoginView.as_view(), name='login'),
   path('logout/', views.LogoutView.as_view(), name='logout'),

   # register
   path('register/', views.RegisterView.as_view(), name='register'),
   path('register/success/',views.RegisterSuccessView.as_view(), name='register-success'),   

   path('accounts/login/', LoginView.as_view(), name='login'),


]
