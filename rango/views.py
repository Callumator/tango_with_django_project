from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Cat
def index(request):
    from rango.models import Student
    student_list = Student.objects.order_by('last_name')
    cats_list = Cat.objects.order_by('name')

    context_dict = {}
    context_dict['Students'] = student_list
    context_dict['Cats'] = cats_list

    for Student in student_list:
        Student.number_of_cats = Cat.objects.filter(Student=Student).count()
        Student.save()

    return render(request, 'rango/index.html', context=context_dict)
def about(request):
    cats_list = Cat.objects.order_by('name')
    context_dict = {}
    context_dict['Cats'] = cats_list
    return render(request, 'rango/about.html', context=context_dict)