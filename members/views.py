from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password


def members(request):
    return HttpResponse("Hello world!")

def students(request):
    return HttpResponse("page for students!")

def create_user(request):
    if request.method == 'GET':
        username = 'BAOLOC2'
        password = '123123'
        user = User.objects.create(username=username, password=password)
        return JsonResponse({'status': 'create success'}, status=200)
    return JsonResponse({'status': 'Invalid request method'}, status=405)

def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'first_name', 'last_name')
        users_list = list(users)
        return JsonResponse(users_list, safe=False, status=200)
    return JsonResponse({'status': 'Invalid request method'}, status=405)