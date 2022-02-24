from django.shortcuts import render
from django.http import HttpResponse
from resume.models import contact
from resume.forms import Nameforms,contactform
from django.contrib import messages

def index_view (request):
    return render(request,'index.html')

def contact_view (request) :
    if request.method =='POST' :
        form=contactform(request.POST)
        if form.is_valid() : 
         form.save()  
         messages.success(request, 'Thank you')    
    form=contactform() 
    return render(request,'contact.html',{'form':form})    
