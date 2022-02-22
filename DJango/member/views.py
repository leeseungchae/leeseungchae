
from django.http import JsonResponse
from django.shortcuts import render

from member.models import Member

# Create your views here.
def signup(request):
    
    if request.method=="GET":
        return render(request,"signup.html")
    
    if request.method=="POST":
        
        
        u_firtname = request.POST.get("first_name")
        u_lastname = request.POST.get("last_name")
        u_eamil = request.POST.get("email")
        u_pw = request.POST.get("pw")
                
        user = Member.objects.create(u_firtname=u_firtname,
                                            u_lastname= u_lastname,
                                            u_eamil =u_eamil,
                                            u_pw =u_pw)
        user.save()
        return render(request,"index.html")
        
def emailch(request):
    # ajax에서 넘어온 user_email값
    email = request.GET.get("user_email")
    
    try:
        qs = Member.objects.get(u_eamil=email)
    except:
        qs:None
    if  qs is None:
        context = {"result":"true"}
    else:
        context = {"result":"false"}
    return JsonResponse(context)
        
