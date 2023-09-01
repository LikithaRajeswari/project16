from django.shortcuts import render

# Create your views here

from app.models import *
from django.http import HttpResponse
def insert_school(request):
    if request.method=='POST':
      Sname=request.POST['Sname']
      Sprinci=request.POST['Sprinci']
      Sloc=request.POST['Sloc']
      So=School.objects.get_or_create(SchName=Sname,SchPricipal=Sprinci,SchLocation=Sloc)[0]
      So.save()
      QLSO=School.objects.all()
      d={'QLSO':QLSO}
      return render(request,'display_schools.html',d)
    return render(request,'insert_school.html')

