from django.shortcuts import render
from .models import *

def home(request):
    template = 'ranking/home.html'
    text = "Coming Soon!"
    if request.method == "POST":
        email = request.POST.get('subscribe-form-email')
        sub = Subscriber(email=email)
        sub.save()
        subscribers = Subscriber.objects.all().count()-1
        text = "Thank You!"
        context = {
            'result': True,
            'email': email,
            'subscribers': subscribers,
            'text': text,
        }
        return render(request, template, context)
    else:
        subscribers = Subscriber.objects.all().count()
        context = {
            'subscribers': subscribers,
            'text': text,
        }
        return render(request, template, context)