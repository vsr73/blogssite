from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import BlogForm
from .models import Blogs
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
        p=request.POST['password']
        q=request.POST['password2']
        if p==q:
            user=User(first_name=f,last_name=l,username=usnm,password=p)
            try:
                user.save()
                messages.info(request,'successfully created')
                return redirect('home')
            except:
                messages.error(request,'username exists')
                return redirect('registeruser')
        else:
            messages.info(request,'passwords doesnt match')
    return render(request,'app/register.html')


def loginuser(request):
    if request.method=='POST':
        p=request.POST['username']
        q=request.POST['password']
        user=User.objects.get(username=p,password=q)
        authenticate(user)
        if user.is_authenticated:
            login(request,user)
            messages.info(request,'successfully logined')
            return redirect('home')
            
        else:
            messages.info(request,'user doesnt exist')
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
        r=request.POST['emaill']
        s=request.POST['message']
        support=blogersupport(name=p,address=q,email=r,message=s)
        try:
            support.save()
            messages.info(request,'response submitted')
            return redirect('home')
        except:
            messages.info(reequest,'error resubmit')
            return redirect('support')

    return render(request,'app/bloggersupport.html')

@login_required(login_url='login')

def userprofile(request,pk):
    user=User.objects.get(id=pk)
    blogs=Blogs.objects.filter(blogger=user).order_by('created').reverse()
    return render(request,'app/profile.html',{'user':user,'blogs':blogs})