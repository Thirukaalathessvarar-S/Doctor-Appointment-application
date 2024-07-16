from django.shortcuts import render,redirect
from .models import User_data,Doctorinfor,Registerinfo
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request,method=['GET','POST']):
    if request.method=='POST':
        email_id = request.POST.get('email')
        password=request.POST.get('password')

        user=User_data.objects.filter(email=email_id,password=password)
        if user.exists():
            request.session['user']=email_id
            return redirect('/home/')
        else:
            messages.error(request,'email and password are incorrect')
    return render(request,'login.html')

    

def signup(request):
    if request.method=="POST":
        x = request.POST.get('email')
        y = request.POST.get('password')
        z = request.POST.get('confirm_password')
        userinfo=User_data.objects.filter(email=x)
        if userinfo.exists():
            messages.error(request,"user already exist")
        elif y!=z:
            messages.error(request,"password not matching")
        else:
            User_data.objects.create(email=x,password=y)
            return render(request,'login.html')
    return render(request,'signup.html')


def home_view(request):
    user=request.session['user']
    Doctor = Doctorinfor.objects.all()
    return render(request,'home.html',{'doctors':Doctor,'user':user})

def register_view(request):
    if request.method=='POST':
        x = request.POST.get('doctor_name')
        y = request.POST.get('p_name')
        z = request.POST.get('date')
        a = request.POST.get('gender')
        b=request.POST.get('contact')
        c=request.POST.get('problem')
        Registerinfo.objects.create(doctor_name=x,p_name=y,date=z,gender=a,contact=b,problem=c)
        return render(request,'success.html')
    return render(request,'register.html')

def book_appoint(request,id):
    doctor_id = Doctorinfor.objects.get(id=id)
    return render(request,'register.html',{'doctor_id':doctor_id})




