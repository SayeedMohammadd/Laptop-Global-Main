from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from publishing.models import publishing
from django.core.paginator import Paginator
from .forms import EditProfile

def login(request):
  if request.method == 'POST':

    user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'Profile details updated.')
      return redirect('index')
    else:
      messages.error(request, 'Profile details updated.')
      return render(request,'accounts/login.html',{'error':'Invalid Email Or Password'})
  else:
    return render(request, 'accounts/login.html')



def signup(request):

  if request.method == 'POST':

    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    cpassword = request.POST['cpassword']

    if len('password')>4:
          if password == cpassword:
              try:
                  user = User.objects.get(username = username)
                  return render(request, 'accounts/signup.html',{'error':'Username Alrady In Use'})
              except User.DoesNotExist:
                  user = User.objects.create_user(username,email,password)
                  auth.login(request,user)
                  return redirect('index')
          else:
              return render(request, 'accounts/signup.html',{'error':'Passwords Must Match'})
    else:
        return render(request, 'accounts/signup.html',{'error':'Passwords Must Be Least 5 Characters'})
  else:
    return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')

def user_profile(request, username):
    user = User.objects.get(username=username)
    publish = publishing.objects.filter(owner=request.user).order_by('-pub_date')
    if request.method == 'GET':
        form = EditProfile(instance=user.profile)
        context = {
            'count':publish.count(),
            'form':form,
        }
        return render(request, 'accounts/profile.html', context)
    else:
        form = EditProfile(request.POST,request.FILES,instance=user.profile)
        if form.is_valid():
                form.save()
                context = {
                    'count':publish.count(),
                    'form':form,
                }
                return render(request,'accounts/profile.html',context)
        else:
            context = {
                'count':publish.count(),
                'form':form,
                'error':'Bad Data'
            }
            return render(request,'accounts/profile.html',context)


def userads(request, username):
    publish = publishing.objects.filter(owner=request.user).order_by('-pub_date')

    paginator = Paginator(publish, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
         'count':publish.count(),
         'page':paged_listings,
         'searched': request.GET
   }
    return render(request,'accounts/userads.html', context)
