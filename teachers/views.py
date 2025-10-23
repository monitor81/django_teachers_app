from django.shortcuts import render
from django.db.models import Q
from .models import Teacher, Discipline

def teacher_list(request):
    query = request.GET.get('q', '')
    teachers = Teacher.objects.all()
    
    if query:
        teachers = teachers.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(disciplines__name__icontains=query)
        ).distinct()
    
    context = {
        'teachers': teachers,
        'query': query,
    }
    return render(request, 'teachers/teacher_list.html', context)

def discipline_list(request):
    query = request.GET.get('q', '')
    disciplines = Discipline.objects.all()
    
    if query:
        disciplines = disciplines.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(teachers__first_name__icontains=query) |
            Q(teachers__last_name__icontains=query)
        ).distinct()
    
    context = {
        'disciplines': disciplines,
        'query': query,
    }
    return render(request, 'teachers/discipline_list.html', context)

def home(request):
    return render(request, 'teachers/home.html')