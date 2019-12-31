#from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from .models import twitter_tweets
from .models import science,commerce,humanity
from .models import keyword_post,collegepages

def home(request):
    return render(request, "home.html", {})

def register(request):
	forms=RegisterForm()
	context = {
	    "forms":forms
	}
	return render(request, "register.html", context )

def login(request):
    return render(request, "login.html", {})

def aboutus(request):
    return render(request, "aboutus.html", {})

def contactus(request):
    return render(request, "contactus.html", {})

def technical(request):
    tweets=twitter_tweets.objects.all()
    courses=science.objects.all()
    posts=keyword_post.objects.all()
    fan=collegepages.objects.all()
    return render(request, "technical.html", { "tweets":tweets,"courses":courses,"posts":posts,"fan":fan })

def postgraduation(request):
    return render(request, "postgraduation.html", {})

def graduation(request):
    return render(request, "graduation.html", {})

def business(request):
    tweets=twitter_tweets.objects.all()
    courses=commerce.objects.all()
    posts=keyword_post.objects.all()
    return render(request, "business.html", { "tweets":tweets,"courses":courses,"posts":posts})


def arts(request):
    tweets=twitter_tweets.objects.all()
    courses=humanity.objects.all()
    posts=keyword_post.objects.all()
    return render(request, "humanity.html", { "tweets":tweets,"courses":courses,"posts":posts})

