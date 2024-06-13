from django.contrib import admin
from django.urls import path
from mind_web import views

urlpatterns = [
    path('https://mind-web-kappa.vercel.app/reg_page',views.registration, name='reg_page'),
    path('https://mind-web-kappa.vercel.app/',views.loginPage, name='login_form'),
    path('https://mind-web-kappa.vercel.app/login',views.loginPage, name='login'),
    path('https://mind-web-kappa.vercel.app/home',views.home, name='home'),
    path('https://mind-web-kappa.vercel.app/contactus', views.contactus, name='contactus'),
    path('https://mind-web-kappa.vercel.app/alphabets', views.alphabets, name='alphabets'),
    path('https://mind-web-kappa.vercel.app/number_table', views.number_table, name='number_table'),
    path('https://mind-web-kappa.vercel.app/mathgame',views.mathgame, name='mathgame'),
    path('https://mind-web-kappa.vercel.app/ADD',views.ADD, name='add'),
    path('https://mind-web-kappa.vercel.app/subtract',views.subtract, name='subtract'),
    path('https://mind-web-kappa.vercel.app/multiply',views.multiply, name='multiply'),
    path('https://mind-web-kappa.vercel.app/divide',views.divide, name='divide'),
    path('https://mind-web-kappa.vercel.app/alpha-game',views.alphagame, name='alpha-game'),
    path('https://mind-web-kappa.vercel.app/alpha-song',views.alphasong, name='alpha-song'),
    path('https://mind-web-kappa.vercel.app/logout',views.LogoutPage,name='logout'),
]