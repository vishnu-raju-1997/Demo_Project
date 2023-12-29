from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . models import *
# Create your views here.
def Homepage(request):
    return render(request,'Homepage.html')

def Medical(request):
    return render(request,'Medical.html')

def Natural(request):
    return render(request,'Natural.html')

def National(request):
    return render(request,'National.html')

def Accident(request):
    return render(request,'Accident.html')

def Earthquake(request):
    return render(request,'Earthquake.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2 :
            user = User1.objects.create_user(username,email,password)
            user.save()
            return redirect('login')
            
   
    return render(request, 'register.html')

def login_view(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username , password = password)

            if user is not None :
                login(request, user)
                return redirect('national')
            
        
        return render(request, 'login.html')



def Wildfire(request):
    return render(request,'Wildfire.html')

def Flood(request):
    return render(request,'Flood.html')

def Volcano(request):
    return render(request,'Volcano.html')

def Caraccident(request):
    return render(request,'caraccident.html')

def Workplace(request):
    return render(request,'workplace.html')

def Service(request):
    return render(request,'service.html')

def Contacts(request):
    return render(request,'contacts.html')

def Border(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaint_text = request.POST.get('complaint')
        uploaded_file = request.FILES.get('file')

        complaint = Complaintboarder.objects.create(name=name, email=email, complaint_text=complaint_text, uploaded_file=uploaded_file)
        complaint.save()

        return redirect('national')
    return render(request,'border.html')

def Cyber(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaint_text = request.POST.get('complaint')
        uploaded_file = request.FILES.get('file')

        complaint = Complaintcyber.objects.create(name=name, email=email, complaint_text=complaint_text, uploaded_file=uploaded_file)
        complaint.save()

        return redirect('national')
    return render(request,'cyber.html')

def Terrorist(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        complaint_text = request.POST.get('Information')
        uploaded_file = request.FILES.get('file')

        complaint = Complaintterror.objects.create(name=name, email=email, complaint_text=complaint_text, uploaded_file=uploaded_file)
        complaint.save()

        return redirect('national')
    return render(request,'terrorist.html')