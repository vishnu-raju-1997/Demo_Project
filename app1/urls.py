from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Homepage,name="Homepage"),
    path('medical/', views.Medical,name="medical"),
    path('natural/', views.Natural,name="natural"),
    path('national/', views.National,name="national"),
    path('accident/',views.Accident,name="accident"),
    path('earthquake/',views.Earthquake,name="earthquake"),
    path('register/',views.register,name="register"),
    path('login/', views.login_view, name="login"),
    path('wildfire/', views.Wildfire,name="wildfire"),
    path('flood/', views.Flood,name="flood"),
    path('volcano/', views.Volcano,name="volcano"),
    path('caraccident/', views.Caraccident,name="caraccident"),
    path('workplace/', views.Workplace,name="workplace"),
    path('service/', views.Service,name="service"),
    path('contacts/', views.Contacts,name="contacts"),
    path('border/', views.Border,name="border"),
    path('cyber/', views.Cyber,name="cyber"),
    path('terrorist/', views.Terrorist,name="terrorist"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)