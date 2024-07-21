
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from . import models

# Create your views here.
def members(request):
    mymembers = models.Member.objects.all().values
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = models.Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember': mymember
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = models.Member.objects.all()
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Mango', 'Ovacado'],
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def testingtwo(request):
    mydata = models.Member.objects.filter(firstname="Mile").values()
    template = loader.get_template('template.html')
    context = {
        'fruits': ['Apple', 'Mango', 'Ovacado'],
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def testingthree(request):
  mydata = models.Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))