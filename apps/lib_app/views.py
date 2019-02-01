from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

from .models import *


def index(request):
    if 'fname' in request.session:
        user = User.objects.get(first_name=request.session['fname'])
        all_messages = Message.objects.all()
        context = {
            'user': user,
            'all_messages': all_messages
            }
        return render(request, 'dashboard.html', context)
    else:
        return render(request,'index.html')

def register(request):
    if request.method == 'GET':
        return render (request, 'register.html')
    if request.method == 'POST':
        check_response = User.objects.registration_validator(request.POST)
    if check_response['valid']:
        request.session['fname'] = check_response['user'].first_name
        return redirect('/quotes') 
    else:
        for error in check_response['errors']:
            messages.add_message(request, messages.ERROR, error)
        return render(request,'register.html')

def login(request):
    errors=[]
    if request.method == 'POST':
        login = User.objects.filter(email=request.POST['email'])
        if login.count() == 1:
            if login[0].password==request.POST['pw']:
                request.session['fname'] = login[0].first_name
                return redirect('/quotes')
            else:
                errors.append("password does not match our records")
        else:
            errors.append("email does not match our records")
        context = {
            'errors': errors
        }
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')

def logout(request):
    request.session.clear()
    return redirect('/')


def show(request):
    if 'fname' in request.session:
        user = User.objects.get(first_name=request.session['fname'])
        all_books = Book.objects.all()
        context = {
            'user': user,
            'all_books': all_books,
            }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')

def add_book(request,id):
    if request.method == 'POST':
        check_response = User.objects.book_validator(request.POST,id)
    user = User.objects.get(first_name=request.session['fname'])
    all_books = Book.objects.all()
    context = {
            'user': user,
            'all_books': all_books
        }
    if check_response['valid']:
        return render(request, 'dashboard.html', context)
    else:
        for error in check_response['errors']:
            messages.add_message(request, messages.ERROR, error)
        return render(request, 'dashboard.html', context)