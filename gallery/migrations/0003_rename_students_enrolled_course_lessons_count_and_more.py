# Generated by Django 5.1.1 on 2024-11-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_course_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='students_enrolled',
            new_name='lessons_count',
        ),
        migrations.RemoveField(
            model_name='course',
            name='rating',
        ),
        migrations.AddField(
            model_name='course',
            name='instructor_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='instructor_image',
            field=models.ImageField(blank=True, null=True, upload_to='instructors/'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=20),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.CharField(choices=[('medical', 'Medical'), ('engineering', 'Engineering'), ('science', 'Science'), ('computer', 'Computer Science'), ('other', 'Other')], default='other', max_length=20),
        ),
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
