from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import book_form
from .models import Books


# Create your views here.
def home(request):
    find_book = Books.objects.all().order_by('-date')
    if request.method == 'POST':
        item = request.POST.get('find')
        if item != '' and item is not None:
            books = find_book
            find_book = find_book.filter(title__icontains=item)

            if len(find_book) == 0:
                messages.info(request, 'Book Not Found')
                return render(request, 'Djapp/home.html', {'books': books})

        return render(request, 'Djapp/home.html', {'books': find_book})

    return render(request, 'Djapp/home.html', {'books': find_book})


def add_book(request):
    if request.method == 'POST':
        form = book_form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = book_form()
    return render(request, 'Djapp/add_book.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'Djapp/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Password is not valid')
    else:
        form = UserCreationForm()
    return render(request, 'Djapp/signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')
