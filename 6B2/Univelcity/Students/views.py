from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def home_page(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})