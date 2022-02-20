from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,"register.html")

def signup(request):
    return render(request,"signup.html")