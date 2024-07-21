
from django import forms
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
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


class CommentForm(forms.ModelForm):

    class Meta:
        model = models.Comment

def add_comment(request, slug, template_name='templates/create.html'):
    post = get_object_or_404(Entry, slug=slug)
    remote_addr = request.META.get('REMOTE_ADDR')

    if request.method == 'post':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            # check spam asynchronously
            tasks.spam_filter.delay(comment_id=comment_id, remote_addr=remote_addr)
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = CommentForm()

    context = RequestContext(request, {'form': form})
    return render_to_response(template_name, context)
        