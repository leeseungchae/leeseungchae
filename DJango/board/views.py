from django.shortcuts import render
from board.models import board

# Create your views here.
def blist(request):
    
    qs = board.objects.all().order_by("-b_no")
    context= {"blist":qs}
    
    
    
    return render(request,"blist.html",context)


def contact(request):
    return render(request,"contact.html")
def elements(request):
    return render(request,"elements.html")
def generic(request):
    return render(request,"generic.html")

