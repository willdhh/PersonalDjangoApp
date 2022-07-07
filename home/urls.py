from django.urls import include, path

from . import views

#app_name = 'home'
urlpatterns = [
    path('', views.homepage,name='home'),
    path('about/', views.aboutpage,name='about'),
    path('experiences/', views.exppage,name='experiences'),
    path('projects/', views.projectpage,name='projects'),
    path('projects/<str:proj_link>/', views.projectdetail,name='projectsdet'),
    path('contacts/', views.contactspage,name='contacts'),
]