from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from publishing.models import publishing

def about(request):
    count_a = publishing.objects.count()
    count_u = User.objects.count()

    return render(request,'about.html',{'count_a':count_a,'count_u':count_u})
