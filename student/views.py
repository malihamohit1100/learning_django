from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
# def profile(request):
#     return HttpResponse("I am inside student profile")

def profile(request):
    print(request.GET.get("name"))
    user_data = {
        "name": "John Doe",
        "age" : 10
    }
    marks = [
        {
            "id": 1,
            "subject": "Math",
            "marks": 90
        },
        {
            "id": 2,
            "subject": "Science",
            "marks": 85
        },
        {
            "id": 3,
            "subject": "English",
            "marks": 95
        }
    ]
    student_data = models.Student.objects.all() 
    print(student_data)
    return render(request, 'student/index.html', {"marks": marks, "age": 20, "Name": "John Doe", "list": ["Math", "Science", "English"], "student_data": student_data})

def home (request):
    return HttpResponse("I am home page")

def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return HttpResponse("Student deleted successfully")

def edit_student(request, id):
    student = models.Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.roll = request.POST.get("roll")
        student.age = request.POST.get("age")
        student.father_name = request.POST.get("father_name")
        student.save()
        return HttpResponse("Student updated successfully")
    return render(request, 'student/edit.html', {"student": student})