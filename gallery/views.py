from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from django.shortcuts import render
from django.templatetags.static import static  # Add this import
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    for course in courses:
        if not course.image:
            course.image_url = static('images/default-course.jpg')
        else:
            course.image_url = course.image.url
    return render(request, 'courses.html', {'courses': courses})


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'course_detail.html', context)


def index(request):
    return render(request, 'index.html')  # Render home.html template

def about_us(request):
    return render(request, 'about_us.html')  # Render home.html template