from django.shortcuts import render
from board.models import board

# 게시판 리스트
def blist(request):
    qs = board.objects.all().order_by("-b_no")
    context= {"blist":qs}
    return render(request,"blist.html",context)

def write(request):
    
    return render(request,"contact.html")




def contact(request):
    return render(request,"contact.html")
def elements(request):
    return render(request,"elements.html")
def generic(request):
    return render(request,"generic.html")

