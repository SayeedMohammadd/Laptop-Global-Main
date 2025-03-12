from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from osm_field.fields import LatitudeField, LongitudeField, OSMField


class publishing(models.Model):
    brand_choices = (
        ('Apple', 'Apple'),
        ('HP', 'HP'),
        ('Acer', 'Acer'),
        ('Asus', 'Asus'),
        ('Dell', 'Dell'),
        ('Lenovo', 'Lenovo'),
        ('MSI', 'MSI'),
        ('Microsoft', 'Microsoft'),
        ('Razor', 'Razor'),
        ('Toshiba', 'Toshiba'),
        ('Google', 'Google'),
        ('Samsung', 'Samsung'),
    )

    fuel_choices = (
        ('0GB', '0GB'),
        ('128GB', '128GB'),
        ('256GB', '256GB'),
        ('512GB', '512GB'),
        ('1000GB', '1000GB'),
        ('2000GB', '2000GB'),
    )
    type_choices = (
        ('Ultrabook', 'Ultrabook'),
        ('Notebook', 'Notebook'),
        ('Gaming', 'Gaming'),
        ('2 in 1', '2 in 1'),
    )

    condition_choices = (
        ('Excellent', 'Excellent'),
        ('Good', 'Good'),
        ('Fairly Good', 'Fairly Good'),
        ('Fairly Poor', 'Fairly Poor'),
        ('Poor', 'Poor'),
    )

    category_choices = (
        ('Used', 'Used'),
        ('New', 'New'),
    )

    title = models.TextField(max_length=100)
    pub_date = models.DateTimeField(default=datetime.now)
    type = models.TextField(max_length=100, choices=type_choices)
    brand = models.TextField(max_length=100, choices=brand_choices)
    model = models.TextField(max_length=50)
    category = models.TextField(max_length=100, choices=category_choices)
    year = models.IntegerField()
    storage = models.TextField(max_length=100, choices=fuel_choices)

    ram = models.IntegerField()
    procesor = models.TextField(max_length=50)
    image1 = models.ImageField(
        upload_to='upload_to=images/%Y/%m/%d/', null=True)
    # image2 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/',null=True)
    # image3 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/',null=True)
    # image4 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/',null=True)
    # image5 = models.ImageField(upload_to='upload_to=images/%Y/%m/%d/',null=True)
    description = models.CharField(max_length=250)
    condition = models.TextField(max_length=100, choices=condition_choices)
    price = models.IntegerField()
    tel = models.TextField(max_length=10)
    city = models.TextField(max_length=50)
    address = models.TextField(max_length=100)
    vote_total = models.IntegerField(default=1)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    location = OSMField()
    location_lat = LatitudeField()
    location_lon = LongitudeField()

    def __str__(self):
        return self.title

  #   def pub_date_pretty(self):
  #       return pub_date.strftime('%b %e %y')
