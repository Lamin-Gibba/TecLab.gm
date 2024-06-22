from django.contrib import admin
from django.urls import path, include
from. import views


urlpatterns = [
    path('', views.Index,name='Index'),
    path('about', views.About,name='About'),
    path('contact', views.Contact,name='Contact'),
    path('mission&vission', views.Mission,name='Mission'),
    path('powers&functions', views.Powersfunctions,name='Powersfunctions'),
    path('project', views.Project,name='Project'),
    path('team', views.Team,name='Team'),
    path('testimonial', views.Testimonial,name='Testimonial'),
    path('service', views.Service,name='Service'),
    path('services', views.Services,name='Services'),
    path('demographic-map', views.Demographic,name='Demographic'),
    path('chairman', views.Chairman,name='Chairman'),
    path('clerk', views.Clerk,name='Clerk'),
    path('ceo', views.Ceo,name='Ceo'),
    path('council', views.Council,name='Council'),
    path('planning&development', views.Planningdevelopment,name='Planningdevelopment'),
    path('council-members', views.Council,name='Council'),
    path('budget&finance', views.Budgetfinance,name='Budgetfinance'),
    path('lands', views.Lands,name='Lands'),
    path('sanitation', views.Sanitation,name='Sanitation'),
    path('education', views.Education,name='Education'),
    path('health', views.Health,name='Health'),
    path('community', views.Community,name='Community'),
    path('agriculture', views.Agriculture,name='Agriculture'),
    path('publication', views.Publications,name='Publications'),
    path('partners', views.Partners,name='Partners'),
    path('int-partners', views.Intpartners,name='Intpartners'),
    path('rates&taxes', views.Ratestaxes,name='Ratestaxes'),
    
    ]
#urlpatterns += static(settings.MEDIA.URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC.URL, document_root=settings.STATIC_ROOT)



