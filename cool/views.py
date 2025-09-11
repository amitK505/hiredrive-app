from django.shortcuts import render,redirect,HttpResponse
from django.urls import path
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import drive
from .models import hire 
from django.template import loader
@login_required(login_url='login')
def home(request):
    
    return render(request,"index.html")
    
    
    
    
def login(request):
    if request.method=="POST":
        if request.POST['username'] =='':
            return render(request,"login.html",{"err":True})
        if request.POST['password'] =='':
            return render(request,"login.html",{"err":True})
        a=request.POST['username']
        b=request.POST['password']
        user=authenticate(request,username=a,password=b)
        if user is not None:
            
        
            return redirect('go')
        else:
            
            return render(request,'login.html',{"error":True})
            
    
    return render(request,"login.html")
def signup(request):
    
    if request.method =="POST":
        a=request.POST['name']
        b=request.POST['last']
        c=request.POST['email']
        d=request.POST['password']
        e=request.POST['password2']
        if d!=e:
            return render(request,'signup.html',{'error':True})
        
        myuser=User.objects.create_user(username=c,email=c,first_name=a,last_name=b, password=d)
        myuser.save()
        return redirect('login')
        
        
        
               
    return render(request,"signup.html")
def logout(request):

    return redirect('home')
def home(request):
    
    
    return render(request,"index.html")
    
def about(request):
    return render(request, 'about.html')
def profile(request):
    return redirect('login')
    

def feedback(request):
    if request.method=="POST":
        c=request.POST.get('submit')
        if c is not None:
            return render(request,'practice.html')

    
    
    return render(request, 'feedback.html')
def practice(request, feedbackid):
    return render(request, 'practice.html', {'feedbackid': feedbackid})
def go(request):
    
    return render(request,'go.html')
def hiredetail(request):
    if request.method=="POST":
        a=request.POST.get("name")
        gg=request.POST.get("fathername")
        b=request.POST.get("religion")
        c=request.POST.get("city")
        d=request.POST.get("nearbylocation")
        e=request.POST.get("mobile")
        f=request.POST.get("mobile2")
        g=request.POST.get("transport")
        h=request.POST.get("aadhar")
        i=request.POST.get("pan")
        aa=request.POST.get("uploadpan")
        bb=request.POST.get("uploadaadhar")
        data2=hire.objects.create(name=a,fathername=gg,religion=b,city=c,nearbylocation=d,mobile=e,alternate_mobile=f,transport=g,aadhar=h, pan=i,uploadpan=aa,uploadaadhar=bb )
        data2.save()
        print(data2)


    return render(request,'hiredetail.html')
def drivedetail(request):
    data=''
    f=""
    if request.method=="POST":
        a=request.POST['name']
        b=request.POST['fathername']
        c=int(request.POST['age'])
        d=request.POST['religion']
        e=request.POST['city']
        f=request.POST['nearbylocation']
        experience=request.POST['experience']
        mobile1=request.POST['mobile1']
        mobile2 =request.POST['mobile2']
        address=request.POST['address']
        permanentaddress = request.POST['permanentaddress']
        dlnumber =request.POST['dlnumber']
        transport=request.POST['transport']
        aadhar=request.POST['aadhar']
        pan=request.POST['pan']
        uploadaadhar = request.FILES.get('uploadaadhar')
        uploadpan = request.FILES.get('uploadpan')
        resume = request.FILES.get('resume')
        data={
            'error':"Driver details already exist in database!",
            
        }
        f={'f':"your age is underage",}
        if (c <18) :
            return render(request,'drivedetail.html',f)
        else:
            if drive.objects.filter(name=a,fathername=b,dlnumber=dlnumber,transport=transport,aadhar=aadhar,pan=pan,religion=d).exists():
                return render(request,'drivedetail.html',data)
            else:
                mydata=drive.objects.create(name=a,fathername=b,age=c,religion=d,city=e,nearbylocation=f,experience=experience,mobile=mobile1,alternate_mobile=mobile2,address=address,permanent_address =permanentaddress ,dlnumber=dlnumber,transport=transport,aadhar=aadhar,pan=pan,uploadpan=uploadpan,uploadaadhar=uploadaadhar,resume=resume )
                mydata.save()
        
       
        
        print(mydata)



    return render(request,'drivedetail.html')
def search(request):
    text=''
    if request.method=="POST":
        name=request.POST.get('name')
        a=request.POST.get('location')
        b=request.POST.get('transport')
        c=request.POST.get('nearbylocation')
        d=request.POST.get('religion')
        aa=request.POST.get('back')
        bb=request.POST.get('submit')
        if drive.objects.filter(name=name).exists():

            jj=hire.objects.filter(city=a,religion=d,transport=b).values()            #common while search dat from database"""
            template=loader.get_template('search.html')
            if not jj:  #if not data found in database
                messages.error(request, "No result found for your search!")
            text={
                'text':jj,
            }
            return HttpResponse(template.render(text,request))
        else:
            messages.error(request, "NAME not found. fill  basic details first than search again") 
            return redirect('drivedetail')



        if aa is not None:
            return redirect('go')
    return render(request,'search.html')
def hiresearch(request):
    if request.method=="POST":
        name=request.POST.get('name')
        location=request.POST.get('location')
        nearbylocation=request.POST.get('nearbylocation')
        religion=request.POST.get('religion')
        transport=request.POST.get('transport')
        condition=request.POST.get('condition')
        if hire.objects.filter( name=name).exists():

            tex=drive.objects.filter( religion=religion,city=location,nearbylocation=nearbylocation,transport=transport).values()
            template=loader.get_template('hiresearch.html')
            if not tex:  #if not data found in database
                messages.error(request, "No result found for your search!")
            text2={
                'text2':tex
            }
            return HttpResponse(template.render(text2,request))
        else:
            messages.error(request, "Fill hire detail FIRST") 
            return redirect('hiredetail')

    return render(request,'hiresearch.html')
def hireback(request):
    return redirect('go')
    
    return render(request,'search.html')
def back(request):
    return redirect('go')
def back2(request):
    return redirect('go')

# Create your views here.
