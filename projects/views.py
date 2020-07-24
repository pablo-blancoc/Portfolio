from django.shortcuts import render
from projects.models import Project


# CREATE A QUERY TO RETRIEVE ALL PROJECTS TO DISPLAY
def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)


# CREATE A QUERY TO RETRIEVE A PROJECT WITH SPECIFIC PRIMARY KEY (pk)
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
