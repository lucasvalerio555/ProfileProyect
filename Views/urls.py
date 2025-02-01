from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.Home, name="Home"),
    path("",views.About, name="About"),
    path("",views.Contact, name="contact"),
    
]

urlpatterns += staticfiles_urlpatterns()