from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BlogForm
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):

    blogs=Blogs.objects.filter().order_by('created').reverse()
    return render(request,'app/home.html',{'blogs':blogs})

def registeruser(request):
    if request.method=='POST':
        f=request.POST['first_name']
        l=request.POST['last_name']
        usnm=request.POST['username']
        el=request.POST['email']
        p=request.POST['password']
        q=request.POST['password2']
        if p==q:
            if len(q)>=8:
                if q.isdigit() == False:
                    if q.islower() == False:
                        if q.isupper() == False:
                            user=User(first_name=f,last_name=l,username=usnm,email=el,password=p)
                            try:
                               user.save()
                               login(request,user)
                               messages.info(request,'successfully created and logged in')
                               return redirect('home')
                            except:
                                messages.error(request,'username exists')
                                return redirect('registeruser')
                        else:
                            messages.info(request,'password must contain atleat 1 lowercase,upper case and a numeric casecharacte')
                            return redirect('registeruser')
                    else:
                        messages.info(request,'password must contain atleat 1 lowercase,upper case and a numeric casecharacter')
                        return redirect('registeruser')
                else:
                    messages.info(request,'password is entirely numeric')
                    return redirect('registeruser')   
            else:
                messages.info(request,'password should contain atleast 8 characters')
                return redirect('registeruser')   
        else:       
            messages.error(request,'password doesnt match')
            return redirect('registeruser')
    else:
        return render(request,'app/register.html')


def loginuser(request):
    if request.method=='POST':
        p=request.POST['username']
        q=request.POST['password']     
        try:
            user=User.objects.get(username=p,password=q)
            f=1

        except:
            f=0
        if f==1:
            authenticate(user)
            if user.is_authenticated:
                login(request,user)
                messages.info(request,'successfully logined')
                return redirect('home')
            else:
                messages.info(request,'retry login')
                return redirect('login')
        else:
            messages.info(request,'details not found try again')
            return redirect('login')
    else:
        return render(request,'app/login.html')
@login_required(login_url='login')
def createblog(request):
    if request.method=='POST':
        p=request.POST['topic']
        q=request.POST['description']
        blog=Blogs(blogger=request.user,topic=p,description=q)
        blog.save()
        return redirect('home')    
    else:
        return render(request,'app/createblog.html')
def logoutuser(request):
    messages.info(request,'logget out successfully')
    logout(request)
    return redirect('home')
def deleteblog(request,pk):
    blog=Blogs.objects.get(id=pk)
    blog.delete()
    messages.info(request,'deleted blog successfully')
    return redirect('home')

def editblog(request,pk):
    blog=Blogs.objects.get(id=pk)
    if request.method == 'POST':
        blog.topic=request.POST['topic']
        blog.description=request.POST['description']
        blog.save()
        messages.info(request,'blog successfully edited')
        return redirect('home')
    else:
        return render(request,'app/editblog.html',{'blog':blog})

def about(request):
    return render(request,'app/about.html')
def bloggersupport(request):

    if request.method == 'POST':
        p=request.POST['name']
        q=request.POST['address']
        r=request.POST['email']
        s=request.POST['message']
        support=blogersupport.objects.create(name=p,address=q,email=r,message=s)
        if len(p)==0 or len(q)==0 or len(r)==0 or len(s) == 0:
            messages.info(request,'please fill all the details')
            return redirect('support')
        else:                 
            try:
                support.save()
                messages.info(request,'request submitted')
                return redirect('home')
            except:
                messages.info(request,'error resubmit')
                return redirect('support')
    else:
        return render(request,'app/bloggersupport.html')

@login_required(login_url='login')
def userprofile(request,pk):
    user=User.objects.get(id=pk)
    blogs=Blogs.objects.filter(blogger=user).order_by('created').reverse()
    return render(request,'app/profile.html',{'user':user,'blogs':blogs})

def editprofile(request,pk):
    user=User.objects.get(id=pk)
    if request.method == 'POST':
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.username=request.POST['username']
        user.email=request.POST['email']
        user.save()
        s=str(user.id)
        messages.info(request,'profile updated')
        return redirect('/profile/'+s)
                
    else:
        return render(request,'app/editprofile.html',{'user':user})

