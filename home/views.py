from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from publishing.models import publishing
from django.core.paginator import Paginator
# map
import pandas as pd
import folium
from folium import plugins
from folium.plugins import MarkerCluster
from django.views.generic import TemplateView


def location_map(request):
    data = pd.read_csv('main_dataset.csv')

    if 'sedan' in request.GET:
        sedan = request.GET['sedan']
        if sedan:
            data = pd.read_csv('types/sedan.csv')

    if 'suv' in request.GET:
        suv = request.GET['suv']
        if suv:
            data = pd.read_csv('types/SUV.csv')

    if 'coupe' in request.GET:
        coupe = request.GET['coupe']
        if coupe:
            data = pd.read_csv('types/coupe.csv')

    if 'pickup' in request.GET:
        pickup = request.GET['pickup']
        if pickup:
            data = pd.read_csv('types/pickup.csv')

    if 'Convertible' in request.GET:
        Convertible = request.GET['Convertible']
        if Convertible:
            data = pd.read_csv('types/convertible.csv')

    if 'Hatchback' in request.GET:
        Hatchback = request.GET['Hatchback']
        if Hatchback:
            data = pd.read_csv('types/hatchback.csv')

    if 'MPV/Minivan' in request.GET:
        MPV = request.GET['MPV/Minivan']
        if MPV:
            data = pd.read_csv('types/mini-van.csv')

    if 'Station Wagon' in request.GET:
        Station = request.GET['Station Wagon']
        if Station:
            data = pd.read_csv('types/wagon.csv')

    if 'van' in request.GET:
        van = request.GET['van']
        if van:
            data = pd.read_csv('types/van.csv')

    if 'lorry' in request.GET:
        lorry = request.GET['lorry']
        if lorry:
            data = pd.read_csv('types/truck.csv')

    lat_lon = data[["lat", "long"]].values[:15000]
    map = folium.Map(location=[35.4676, -97.5164],
                     tiles='CartoDB dark_matter', zoom_start=4)
    marker_cluster = MarkerCluster().add_to(map)

    for point in range(0, 1000):
        folium.Marker(lat_lon[point], popup=data['type'][point], icon=folium.Icon(
            color='darkblue', icon_color='white', icon='car', angle=0, prefix='fa')).add_to(marker_cluster)

    map = map._repr_html_()
    context = {
        'nodes': map,
    }

    return render(request, 'location_map.html', context)


def index(request):
    publish = publishing.objects.order_by('-pub_date')

    return render(request, 'index.html', {'publish': publish, 'count': publish.count()})


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # send Email
        send_mail(
            subject,  # Subject
            message + ' from '+email,  # message
            email,  # from
            ['denukasandeepa@gmail.com'],  # to
        )

        return render(request, 'contact.html', {'name':  name})
    else:
        return render(request, 'contact.html')


def type(request):
    type = publishing.objects.order_by('-pub_date')

    if 'Apple' in request.GET:
        apple = request.GET['Apple']
        if apple:
            type = type.filter(type__icontains=apple)

    if 'HP' in request.GET:
        hp = request.GET['HP']
        if hp:
            type = type.filter(type__icontains=hp)

    if 'Dell' in request.GET:
        dell = request.GET['Dell']
        if dell:
            type = type.filter(type__icontains=dell)

    if 'Google' in request.GET:
        google = request.GET['Google']
        if google:
            type = type.filter(type__icontains=google)

    if 'Lenovo' in request.GET:
        lenovo = request.GET['Lenovo']
        if lenovo:
            type = type.filter(type__icontains='lenovo')

    if 'Toshiba' in request.GET:
        Toshiba = request.GET['Toshiba']
        if Toshiba:
            type = type.filter(type__icontains='Toshiba')

    paginator = Paginator(type, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'count': type.count(),
        'page': paged_listings,
        'searched': request.GET
    }
    return render(request, 'publishing/search.html', context)
