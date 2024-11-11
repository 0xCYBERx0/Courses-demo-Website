from django.db import models
from django.utils.text import slugify

class Course(models.Model):
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    CATEGORY_CHOICES = [
        ('medical', 'Medical'),
        ('engineering', 'Engineering'),
        ('science', 'Science'),
        ('computer', 'Computer Science'),
        ('other', 'Other')
    ]
    
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ]

    # Basic Information
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(default="Course description coming soon")
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    
    # Course Details
    duration = models.CharField(max_length=50)
    students = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lessons_count = models.IntegerField(default=0)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='beginner')
    video_url = models.URLField(max_length=200, blank=True, help_text="Enter YouTube video URL", null=True)
    video_description = models.TextField(max_length=200, blank=True, help_text="Enter YouTube Description", null=True)
    
    # Instructor Information
    instructor_name = models.CharField(max_length=100)
    instructor_title = models.CharField(max_length=100)
    instructor_image = models.ImageField(upload_to='instructors/', blank=True, null=True)
    instructor_description = models.TextField(blank=True)
    
    # Additional Information
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title