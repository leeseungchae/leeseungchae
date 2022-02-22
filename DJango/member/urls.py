
from django.urls import path,include
from .import views
app_name = "member"
urlpatterns = [
    
    
    path("signup",views.signup,name="signup"),
    path("emailch",views.emailch,name="emailch")
   
]
