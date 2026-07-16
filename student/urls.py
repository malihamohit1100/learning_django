from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name = "student_profile"),
    path('home/', views.home, name = "student_home"),
    path('delete/<int:id>/', views.delete_student, name = "delete_student"),
    path('edit/<int:id>/', views.edit_student, name = "edit_student"),
]