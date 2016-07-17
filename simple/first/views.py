from django.shortcuts import render,get_object_or_404
#from django.template import loader
from django.http import Http404
from .models import Question

def index(request,question_id):
    q=get_object_or_404(Question,id=question_id)
    return render(request,'first/index.html',{'data':q})

def details(request):
    q=Question.objects.all()
    context={'data':q,}
    return render(request,'first/details.html',context)




