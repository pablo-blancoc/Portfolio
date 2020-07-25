from django.shortcuts import render
from pages.models import Skill

# Create your views here.
def home(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'home.html', context)