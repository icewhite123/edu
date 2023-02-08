from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView,DetailView
from .models import *

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class About(TemplateView):
    template_name = 'about.html'

class Contact(CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = "__all__"

class Course(ListView):
    model = Course
    paginate_by = 3
    template_name = 'course.html'

class Team(ListView):
    model = Instructor
    template_name = 'team.html'

class Detail(DetailView):
    model=Course
    template_name = 'detail.html'

class Feature(TemplateView):
    template_name = 'feature.html'

class Testimonial(TemplateView):
    template_name = 'testimonial.html'










