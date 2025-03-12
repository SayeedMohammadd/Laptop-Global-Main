from ast import Try
from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateAdForm
from .models import publishing
from accounts.models import Profile
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from django.urls import reverse_lazy, reverse
import pickle
import numpy as np
from .forms import PredictForm
import joblib
import numpy as np
import pandas as pd

# Create your views here.


@login_required(login_url='login')
def posting(request):
    if request.method == 'GET':
        return render(request, 'publishing/publishing.html', {'form': CreateAdForm()})

    else:
        form = CreateAdForm(request.POST, request.FILES or None)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.owner = request.user
            newform.save()
            return HttpResponseRedirect(reverse('ads'))

        return render(request, 'publishing/publishing.html', {'form': CreateAdForm()})


def detail(request, publish_id):
    publish = get_object_or_404(publishing, pk=publish_id)
    related = publishing.objects.filter(type=publish.type).order_by(
        '-pub_date').exclude(id=publish.id)

    return render(request, 'publishing/details.html', {'publish': publish, 'related': related})


def likes(request, publish_id):
    if request.method == 'POST':
        publish = get_object_or_404(publishing, pk=publish_id)
        publish.vote_total += 1
        publish.save()

        return redirect('/publishing/' + str(publish.id))


def ads(request):
    count = publishing.objects.count()
    publish = publishing.objects.order_by('-pub_date')

    paginator = Paginator(publish, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    return render(request, 'publishing/ads.html', {'page': paged_listings, 'count': count})


def update(request, publish_id):
    publish = get_object_or_404(publishing, pk=publish_id)
    if request.method == 'GET':
        form = CreateAdForm(instance=publish)
        return render(request, 'publishing/updatead.html', {'publish': publish, 'form': form})
    else:

        form = CreateAdForm(request.POST, request.FILES, instance=publish)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.owner = request.user
            newform.save()
            return redirect('/publishing/' + str(publish.id))
        else:
            return render(request, 'publishing/updatead.html', {'publish': publish, 'form': form, 'error': 'Bad Data'})


@login_required
def delete(request, publish_id):
    delete = get_object_or_404(publishing, pk=publish_id)
    if request.method == 'POST':
        delete.delete()
        return HttpResponseRedirect(reverse('ads'))


def search(request):
    adlist = publishing.objects.order_by('-pub_date')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            adlist = adlist.filter(title__icontains=keyword)

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            adlist = adlist.filter(category__icontains=category)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            adlist = adlist.filter(model__icontains=model)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            adlist = adlist.filter(year__iexact=year)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            adlist = adlist.filter(city__icontains=city)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            adlist = adlist.filter(transmission__iexact=transmission)

    paginator = Paginator(adlist, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'count': adlist.count(),
        'page': paged_listings,
        'searched': request.GET
    }
    return render(request, 'publishing/search.html', context)


def predict(request):
    if request.method == 'GET':
        return render(request, "publishing/prediction.html", {'form': PredictForm()})


def results(request):
    if request.method == "POST":

        pipe = pickle.load(open('pipe.pkl', 'rb'))
        # f = PredictForm(request.POST)
        # if f.is_valid() or not f.is_valid():
        cpu = request.POST.get("cpu")
        company = request.POST.get("company")
        type = request.POST.get("type")
        ram = request.POST.get("ram")
        ips = request.POST.get("ips")
        resolution = request.POST.get("resolution")
        weight = request.POST.get("weight")
        screensize = request.POST.get("screensize")
        touchscreen = request.POST.get("touchscreen")
        hdd = request.POST.get("hdd")
        ssd = request.POST.get("ssd")
        gpu = request.POST.get("gpu")
        os = request.POST.get("os")
        X_Res = int(resolution.split('x')[0])

        Y_Res = int(resolution.split('x')[1])

        ppi = ((int(X_Res)**2)+(int(Y_Res)**2))**0.5/float(screensize)
        # else:
        #     return HttpResponseRedirect('/')
    query = np.array([company, type, int(ram), float(weight),
                      int(touchscreen), int(ips), int(ppi), cpu, int(hdd), int(ssd), gpu, os])
    query = query.reshape(1, 12)
    price = str((int(np.exp(pipe.predict(query)[0])))*4.55)
    context = {
        'company': company,
        'type': type,
        'ram': ram,
        'weight': weight,
        'touchscreen': touchscreen,
        'ips': ips,
        'ppi': ppi,
        'cpu': cpu,
        'hdd': hdd,
        'ssd': ssd,
        'os': os,
        'gpu': gpu,
        'predict_value': ("%.2f" % float(price)),

    }
    # return HTTPResponse("Page was found")
    # return render(request,"publishing/prediction.html",{'form' : PredictForm()})
    return render(request, "publishing/results.html", context)
