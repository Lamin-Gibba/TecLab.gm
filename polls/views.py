from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Service(request):
    return render(request, 'service.html')

def Services(request):
    return render(request, 'services.html')

def Contact(request):
    return render(request, 'contact.html')

def Project(request):
    return render(request, 'project.html')

def Testimonial(request):
    return render(request, 'testimonial.html')
    
def Sanitation(request):
    return render(request, 'sanitatione.html')

def Education(request):
    return render(request, 'education.html')

def Team(request):
    return render(request, 'team.html')

def Error(request):
    return render(request, '404.html')

def Health(request):
    return render(request, 'health.html')

def Community(request):
    return render(request, 'community.html')

def Agriculture(request):
    return render(request, 'agriculture.html')

def Community(request):
    return render(request, 'community.html')

def Lands(request):
    return render(request, 'lands.html')

def Mission(request):
    return render(request, 'mission&vission.html')

def Powersfunctions(request):
    return render(request, 'powers&functions.html')

def Demographic(request):
    return render(request, 'demographic-map.html')

def Chairman(request):
    return render(request, 'chairman.html')

def Clerk(request):
    return render(request, 'clerk.html')

def Ceo(request):
    return render(request, 'ceo.html')

def Planningdevelopment(request):
    return render(request, 'planning&development.html')

def Council(request):
    return render(request, 'council-members.html')

def Ratestaxes(request):
    return render(request, 'rates&taxes.html')

def Budgetfinance(request):
    return render(request, 'Budget&finance.html')

def Partners(request):
    return render(request, 'partners.html')

def Intpartners(request):
    return render(request, 'int-partners.html')

def Publications(request):
    return render(request, 'publication.html')

def Sanitation(request):
    return render(request, 'sanitation.html')





