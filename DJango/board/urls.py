
from django.urls import path,include
from . import views
app_name = "board"
urlpatterns = [
    #게시판
    path("blist", views.blist ,name="blist"),
    path("write", views.write ,name="write"),
    
    
    
    
    path("contact", views.contact ,name="contact"),
    path("elements", views.elements ,name="elements"),
    path("generic", views.generic ,name="generic"),

   
]
