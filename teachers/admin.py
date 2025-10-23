from django.contrib import admin
from .models import Teacher, Discipline

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'email')
    list_filter = ('disciplines',)
    search_fields = ('last_name', 'first_name', 'middle_name', 'email')
    filter_horizontal = ('disciplines',)