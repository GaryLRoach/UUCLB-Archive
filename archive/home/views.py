from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'home/main.html')


def welcome(request):
    return render(request, "home/welcome.html")