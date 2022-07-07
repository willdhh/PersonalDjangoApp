from pickle import TRUE
from django.db import models
from django import forms


class HomePage(models.Model):    
    title_text = models.CharField(max_length=200)
    link_text = models.CharField(max_length=200, null=TRUE)
    quick_intro = models.TextField()
    introphoto = models.ImageField(upload_to= 'images/home/', blank = True)
    def __str__(self):
        return self.title_text
    
class Intro(models.Model):
    indexitem = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    intro = models.TextField()
    def __str__(self):
        return self.intro
        
class AboutPage(models.Model):
    section_title = models.CharField(max_length=200)
    bodytext = models.TextField()
    
    def __str__(self):
        return self.section_title


class ExpPage(models.Model):
    
    exptitle = models.CharField(max_length=200)
    expduration = models.CharField(max_length=200,blank=True)
    
    def __str__(self):
        return self.exptitle

class ExpBody(models.Model):
    
    exptitle = models.ForeignKey(ExpPage, on_delete=models.CASCADE)
    expbody = models.TextField(blank=True)
    
    def __str__(self):
        return self.expbody
    
class ProjectPage(models.Model):
    
    project_title = models.CharField(max_length=200)
    project_description = models.TextField(max_length=200)
    project_link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.project_title
    
class ProjectDetail(models.Model):
    project = models.ForeignKey(ProjectPage, on_delete=models.CASCADE)
    project_detail = models.TextField()
    def __str__(self):
        return self.project_detail
    
class ContactPage(forms.Form):    
    sender = forms.CharField(required=True)
    yourcontact = forms.CharField(required=False)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':6,'cols':22, 'style':'resize:none;'}))