from django.shortcuts import render

# Create your views here.
def fruit_students_list(request):
    fruits = ['Apple', 'Banana', 'Orange', 'Mango', 'Pineapple']
    students = ['John', 'Jane', 'Mike', 'Sarah', 'Tom']
    return render(request, 'Lists/list.html',{'fruits':fruits,'students':students})