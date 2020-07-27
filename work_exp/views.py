from django.shortcuts import render
from work_exp.models import Company, Certificate


# Create your views here.
def work_exp(request):
    companies = Company.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'companies': companies,
        'certificates': certificates
    }
    return render(request, 'work_exp.html', context)