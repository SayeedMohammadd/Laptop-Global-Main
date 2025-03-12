from django.urls import path
from publishing import views as detail_views
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('',views.index,name ='index'),
    path('contact/',views.contact,name ='contact'),
    path('<int:publish_id>',detail_views.detail, name='details'),
    path('<int:publish_id>/likes',detail_views.likes, name='likes'),
    path('type', views.type, name='type'),
    path('location_map', views.location_map, name='location_map'),

]
