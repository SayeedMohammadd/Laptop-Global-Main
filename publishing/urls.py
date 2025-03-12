from django.urls import path
from . import views

urlpatterns = [
    path('', views.posting, name='publishing'),
    path('ads', views.ads, name='ads'),
    path('<int:publish_id>', views.detail, name='details'),
    path('<int:publish_id>/likes', views.likes, name='likes'),
    path('<int:publish_id>/update', views.update, name='update'),
    path('<int:publish_id>/delete', views.delete, name='delete'),
    path('deletd', views.delete, name='deleted'),
    path('search', views.search, name='search'),
    path('results', views.results, name='results'),
    path('predict', views.predict, name='predict'),


]
