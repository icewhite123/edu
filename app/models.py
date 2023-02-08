from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    courses = (
        ("Python", "Python"),
        ("Java", "Java"),
        ("C++", "C++"),
        ("C#", "C#"),
        ("Frontend", "Frontend")
    )
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    course = models.CharField(choices=courses, max_length=40)

    def __str__(self):  
        return self.name

    def get_absolute_url(self):
        return reverse('contact')

class Instructor(models.Model):
    photo = models.ImageField(upload_to="img/")
    name = models.CharField(max_length=20)
    profession = models.CharField(max_length=35)

    def __str__(self):  
        return self.name

    
class Course(models.Model):
    photo = models.ImageField(upload_to="img/")
    mentors = (
        ("Madina", "Madina"),
        ("Sherzod", "Sherzod"),
        ("Sunnat", "Sunnat"),
        ("Shahnoza", "Shahnoza")
    )
    course = models.CharField(max_length=150)
    mentor = models.CharField(choices=mentors, max_length=50)
    raiting = models.IntegerField(max_length=10)
    voices = models.CharField(max_length=50)
    about_course=models.TextField()



    

