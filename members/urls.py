from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('tutors/', views.students, name='students'),
    path('create_user/', views.create_user, name='create_user'),
    path('get_all_users/', views.get_all_users, name='get_all_users'),  # New URL pattern
]