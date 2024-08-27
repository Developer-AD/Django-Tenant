from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *
from django.contrib import messages

# Create your views here.
def home(request):
    students = Student.objects.all()
    print('----------------------------------------')
    print(students)
    stds = [(std.roll, std.name) for std in students]
    print('----------------------------------------')
    return HttpResponse(f"Client URL : {request.tenant} : {stds}")

# ------------ Upload Data Starts ------------------


# @login_required(login_url="/login")
def student_add(request, roll, name):

    Student.objects.create(name=name, roll=roll)
    messages.success(
        request, "Student record has been created successfully")

    return HttpResponse(f'{request.tenant} :- Student : {name} created successfully')
    # ---------------------------------------------

    # if request.method == 'POST':
    #     roll = request.POST.get('roll')
    #     name = request.POST.get('name')

    #     email = request.POST.get('email')
    #     age = request.POST.get('age')
    #     phone = request.POST.get('phone')
    #     photo = request.FILES.get('photo')

    #     print('-------------- Student Details Start -----------------')
    #     print(name)
    #     print(email)
    #     print(age)
    #     print(phone)
    #     print(photo)
    #     print('-------------- Student Details End -----------------')

    #     Student.objects.create(name=name, roll=roll)
    #     messages.success(
    #         request, "Student record has been created successfully")

    #     return HttpResponse(f'{request.tenant} :- Student : {name} created successfully')
    # return render(request, 'student_add.html')