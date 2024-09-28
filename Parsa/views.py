from django.shortcuts import render
from contact_app.models import Contact
from project_app.models import Project


def site(request):
    projects = Project.objects.all()
    name = request.POST.get('name')
    lastname = request.POST.get('lastname')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    body = request.POST.get('body')
    if name and lastname and email and phone:
        Contact.objects.create(name=name, lastname=lastname, email=email, phone=phone, body=body)
    return render(request, 'index.html', {'projects': projects})
