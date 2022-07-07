from django.contrib import admin

from .models import HomePage, Intro, AboutPage, ExpPage, ExpBody, ProjectPage, ProjectDetail

    
class IntroAdmin(admin.StackedInline):
    model = Intro
    
class ExpBodyAdmin(admin.StackedInline):
    model = ExpBody  
    
class ProjectDetailAdmin(admin.StackedInline):
    model = ProjectDetail    
    

class HomeAdmin(admin.ModelAdmin):
    model = HomePage
    fields = ('title_text','link_text','quick_intro','introphoto',)
    ordering = ['pk']
 
    list_display = ('title_text','link_text','quick_intro',)
    list_editable = ('link_text','quick_intro',)
    inlines = [IntroAdmin]
    
class ExpAdmin(admin.ModelAdmin):
    model = ExpPage
    fields = ('exptitle','expduration')
    ordering = ['pk']
 
    list_display = ('exptitle','expduration')
    inlines = [ExpBodyAdmin]
    
class ProjectAdmin(admin.ModelAdmin):
    model = ProjectPage
    ordering = ['pk']
    inlines = [ProjectDetailAdmin]
    

admin.site.register(HomePage, HomeAdmin)
admin.site.register(AboutPage)
admin.site.register(ExpPage, ExpAdmin)
admin.site.register(ProjectPage, ProjectAdmin)