from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import CreateUserForm
from django.db.models import Q


# Create your views here.


def main(request):
    if request.user.is_authenticated:
        return redirect("home")
        
    return render(request, template_name='chat/main.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password is incorrect")
            return render(request, template_name='chat/login.html')
    return render(request, template_name='chat/login.html')

def register(request):
    form = CreateUserForm()
    context = {
        'form': form,
    }
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account was successfully created for " + user)
            return redirect("login-view")
        else:
            messages.error(request, "Invalid data input ")
            return render(request, template_name='chat/register.html', context=context)
            
    return render(request, template_name='chat/register.html', context=context)

@login_required(login_url="login-view")
def logout_view(request):
    logout(request)
    return redirect("main")

@login_required(login_url="login-view")
def home(request):
   if request.user.is_authenticated:
    users = User.objects.all()
    context = {'user': request.user,
        "users":users}
    return render(request, template_name='chat/home.html', context=context)


@login_required(login_url="login-view")
def chat_person(request,id):
    person = User.objects.get(id=id)
    me = request.user
    messages = Message.objects.filter(Q(from_who=me, to_who=person) | Q(to_who=me, from_who=person)).order_by("date", "time")
    
    context = {
        "person":person,
        "me":me,
         "messages":messages
    }
    return render(request, template_name='chat/chat_person.html', context=context)