from django.shortcuts import render, HttpResponse, redirect
from .models import Student
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .forms import RegistrationForm 

def show(request):
    return render(request, "home.html")

def all_students(request):
    students = Student.objects.all()
    context = {
        'studs': students
    }
    print(context)
    return render(request, 'viewstudent.html', context)

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        s_name = request.POST['s_name']
        s_fathername = request.POST['s_fathername']
        s_mothername = request.POST['s_mothername']
        s_addr = request.POST['s_addr']
        previous_school = request.POST['previous_school']  
        s_phone = request.POST['s_phone']  
        s_gender = request.POST['s_gender']
        s_class = request.POST['s_class']

        
        student_count = Student.objects.count()
        new_student = Student(
            s_name=s_name,
            s_fathername=s_fathername,
            s_mothername=s_mothername,
            s_addr=s_addr,
            previous_school=previous_school,
            s_phone=s_phone,
            s_gender=s_gender,
            s_class=s_class,
        )
        new_student.save()
        new_student_id = new_student.id  
        messages.success(request, f"Student with ID {new_student_id} has been added successfully")
        return redirect('register')

    elif request.method == 'GET':
        return render(request, 'register.html', {'form' :   form})
    else:
        return HttpResponse("Exception Occurred")

def delete_student(request, student_id=0):
    if student_id:
        try:
            student_to_be_removed = Student.objects.get(id=student_id)
            student_to_be_removed.delete()
            messages.success(request, "Student has been deleted successfully")
            return redirect('delete_student')
            
        except Student.DoesNotExist:
            return HttpResponse("Please enter a valid student ID")
            
    students = Student.objects.all()
    context = {
        'students': students
    }
    print(context)
    return render(request, 'delete_student.html', context)

def update_student(request, id):
    print("Student ID:", id)
    student = Student.objects.get(id=id)
    context = {
        "student": student,
    }
    return render(request, 'update_student_details.html', context)

def student_update(request, id):
    print("Student ID:", id)
    if request.method == 'POST':
        student_id = request.POST.get('student_id', id)
        s_name = request.POST['s_name']
        s_fathername = request.POST['s_fathername']
        s_mothername = request.POST['s_mothername']
        s_addr = request.POST['s_addr']
        previous_school = request.POST['previous_school']
        s_phone = request.POST['s_phone']
        s_gender = request.POST['s_gender']
        s_class = request.POST['s_class']

        student = Student.objects.get(id=student_id)
        student.s_name = s_name
        student.s_fathername = s_fathername
        student.s_mothername = s_mothername
        student.s_addr = s_addr
        student.previous_school = previous_school
        student.s_phone = s_phone
        student.s_gender = s_gender
        student.s_class = s_class
        student.save()
        messages.success(request, "Your student profile has been updated successfully")
        return redirect('delete_student')

    return render(request, 'update_student_details.html')
