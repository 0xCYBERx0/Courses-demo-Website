from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'instructor_name', 'duration', 'students']
    list_filter = ['category', 'instructor_name']
    search_fields = ['title', 'description', 'instructor_name' 'lessons_count']
    
    fieldsets = [
        ('Basic Information', {
            'fields': ['title', 'category', 'description']
        }),
        ('Course Details', {
            'fields': ['duration', 'students', 'instructor_name', 'instructor_title']
        }),
        ('Video Content', {
            'fields': ['video_url', 'video_description'],
            'classes': ['collapse']
        })
    ]