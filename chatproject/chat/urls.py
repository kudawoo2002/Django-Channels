from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('login/', views.login_view, name="login-view"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout_view, name="logout-view"),
    path('home/', views.home, name="home"),
    path('chat_person/<int:id>', views.chat_person, name="chat_person"),
]