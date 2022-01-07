from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Views are more of request handlers
def index(request):
    print("Hello, world")
    return HttpResponse("<h1>Hello, world</h1>")


def welcome(request):
    print("Welcome page")
    return render(request, "home.html", {"name": "Michael"})
