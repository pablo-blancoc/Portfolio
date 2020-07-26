from django.urls import path
from work_exp import views

urlpatterns = [
    path('', views.work_exp, name='work_exp'),
]