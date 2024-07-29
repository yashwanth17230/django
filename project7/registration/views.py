from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Student, Course, Enrollment
from .forms import EnrollmentForm

def register_student(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/registration/success/')
    else:
        form = EnrollmentForm()

    return render(request, 'registration/register_student.html', {'form': form})

def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = Enrollment.objects.filter(course=course)
    return render(request, 'registration/course_students.html', {'course': course, 'students': students})