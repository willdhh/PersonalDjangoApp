from django.shortcuts import get_object_or_404, render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import HomePage, AboutPage, ExpPage, ProjectPage, ContactPage, ProjectDetail


    
def homepage(request):
    return render(request, 'home/homepage.html', {"intro":introContext(1),})

def aboutpage(request):
    body = AboutPage.objects.all()
    pk = 1    
    return render(request, 'home/about/about.html', {"intro":introContext(2), "pk":pk, "body":body})

def exppage(request):
    body = ExpPage.objects.all()
    pk = 2    
    return render(request, 'home/experiences/experiences.html', {"intro": introContext(3), "pk":pk, "body":body})

def projectpage(request):
    pk = 3
    body = ProjectPage.objects.all().order_by('pk')
    if request.method == 'GET':     
        return render(request, 'home/projects/projects.html', {"intro": introContext(4), "pk":pk,"projects":body})

def projectdetail(request, proj_link):
    
    project = ProjectDetail.objects.get(project__project_link = proj_link)
    resizer = False
    if(proj_link == 'resizer'):
        resizer = True
    
    return render(request, 'home/projects/resizer.html',{"project": project, "resizer": resizer})

def contactspage(request):
    body = AboutPage.objects.all()
    pk = 4 
    
    if request.method == 'GET':
        form = ContactPage()
    else:
        form = ContactPage(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            returnaddresss= form.cleaned_data['yourcontact']
            
            message = 'from: ' + sender + '/n' + message 
            try:
                send_mail(subject, message, returnaddresss, ['willdhhwang@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/contacts/')
    return render(request, "home/contacts/contacts.html", {'form': form, "intro":introContext(5), "body":body, "pk":pk})

    
def introContext(key):    
    return get_object_or_404(HomePage, pk = key) 


    