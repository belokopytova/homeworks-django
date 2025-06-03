from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    context = {'object_list' : Student.objects.order_by('group'), 'teachers_': Teacher.objects.all()}

    return render(request, template, context)

