from concurrent.futures.process import _python_exit
from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST('name')
        age = request.POST('age')
        phone = request.POST('phone')
        email = request.POST('email')
        message = request.POST('message')

        contact.name = name
        contact.age = age
        contact.phone = phone
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
        
    return render(request, 'contact.html')