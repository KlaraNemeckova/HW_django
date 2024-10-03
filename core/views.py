from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def core_new(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())


def home_page(request):
    return render(request, "home.html")


def about_page(request):
    return render(request, "about.html")


def contact_page(request):
    return render(request, "contact.html")


def core(request):
    return HttpResponse("Hello world!")