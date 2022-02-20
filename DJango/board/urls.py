
from django.urls import path,include
from . import views
app_name = "board"
urlpatterns = [
    path("blist", views.blist ,name="blist"),
    path("contact", views.contact ,name="contact"),
    path("elements", views.elements ,name="elements"),
    path("generic", views.generic ,name="generic"),

   
]
