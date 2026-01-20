from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# List Students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# Add Student
def student_add(request):
    if request.method == "POST":
        Student.objects.create(
            roll_no=request.POST.get('roll_no'),
            name=request.POST.get('name'),
            student_class=request.POST.get('student_class'),
            father_name=request.POST.get('father_name'),
            mother_name=request.POST.get('mother_name'),
            mobile_no=request.POST.get('mobile_no'),
            blood_group=request.POST.get('blood_group'),
        )
        return redirect('student_list')
    return render(request, 'student_add.html')

# Update Student
def student_update(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.roll_no = request.POST.get('roll_no')
        student.name = request.POST.get('name')
        student.student_class = request.POST.get('student_class')
        student.father_name = request.POST.get('father_name')
        student.mother_name = request.POST.get('mother_name')
        student.mobile_no = request.POST.get('mobile_no')
        student.blood_group = request.POST.get('blood_group')
        student.save()

        return redirect('student_list')

    return render(request, 'student_update.html', {'student': student})

# Delete Student
def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')
