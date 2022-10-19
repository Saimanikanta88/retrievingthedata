from django.shortcuts import render
from django.db.models.functions import Length
# Create your views here.
from app.models import *

def display_topic(request):
    T=Topic.objects.all().order_by(length('topic_name'))
    d={'topics':T}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    W=Webpage.objects.all()
    W=Webpage.objects.all().order_by('topic_name')
    W=Webpage.objects.all().order_by('-topic_name')
    W=Webpage.objects.all().filter(topic_name='carrom').order_by('name')
    W=Webpage.objects.all().filter(topic_name='chess')
    W=Webpage.objects.order_by(Length('topic_name').desc())
    W=Webpage.objects.all()[1:5:]
    d={'webpages':W}
    return render(request,'display_webpage.html',d)
    

def accessrecords(request):
    A=Accessrecords.objects.all()
    d={'accessrecords':A}
    return render(request,'display_accessrecords.html',d)



