from django.shortcuts import render
from work_exp.models import Company


# Create your views here.
def work_exp(request):
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, 'work_exp.html', context)