
from django.contrib import admin


from django.urls import path,include
from website import views
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('contact.html', views.contact,name="contact"),
    
 
]
