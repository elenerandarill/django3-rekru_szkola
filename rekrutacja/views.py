import sys

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, FormUczen


def home(request):
    title = 'Strona Glowna'
    return render(request, 'rekrutacja/home.html', {'title': title})


def rejestracja(request):
    title = 'Rejestracja'
    if request.method == 'GET':
        form = UserRegisterForm()
        return render(request, 'rekrutacja/rejestracja.html', {'title': title, 'form': form})
    else:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało utworzone. Możesz się zalogować.')
            return redirect('home')


def logowanie(request):
    title = 'Logowanie'
    form = AuthenticationForm()
    if request.method == 'GET':
        return render(request, 'rekrutacja/logowanie.html', {'title': title, 'form': form})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Login i hasło nie pasują.')
            return render(request, 'rekrutacja/logowanie.html', {'title': title, 'form': form})


@login_required
def wyloguj(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@login_required
def aplikuj(request):
    title = 'Aplikuj'
    return render(request, 'rekrutacja/aplikuj.html', {'title': title})


@login_required
def formuczen(request):
    title = 'Uczniowie'
    if request.method == 'GET':
        form = FormUczen()
        return render(request, 'rekrutacja/formuczen.html', {'title': title, 'form': form})
    else:
        form = FormUczen(request.POST)
        if form.is_valid():
            new_f = form.save(commit=False)
            new_f.uzytkownik = request.user     # Makes the logged user the owner of the form.
            new_f.save()
            messages.success(request, 'Dziękujemy za wysłanie formularza.')
            return redirect('home')
        else:
            messages.error(request, 'Błędnie wprowadzone dane.')
            return render(request, 'rekrutacja/formuczen.html', {'title': title, 'form': FormUczen(request.POST)})
