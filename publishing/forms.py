from django import forms
from .models import publishing
from django.utils.translation import ugettext_lazy as _


class CreateAdForm(forms.ModelForm):
    class Meta:
        model = publishing
        fields = (
            'title',
            'type',
            'brand',
            'model',
            'category',
            'year',
            'procesor',
            'ram',
            'storage',
            'image1',
            # 'image2',
            # 'image3',
            # 'image4',
            # 'image5',
            'description',
            'condition',
            'price',
            'tel',
            'city',
            'address',
            'location',
            'location_lat',
            'location_lon',
        )

        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Ad title.... e.g- ASUS VivoBook i5 11th Laptop"}),
            'description': forms.Textarea(attrs={"placeholder": "Your advertisement information including Laptop Specification, Condition, Warranty and your Contact information..."}),
            'type': forms.Select(attrs={"class": "form-control"}),
            'brand': forms.Select(attrs={"class": "form-control"}),
            'model': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the correct Model.... eg- VivoBook X515E"}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'year': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Without spaces or any symbols or letters"}),

            'ram': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Without spaces or any symbols or letters"}),
            'storage': forms.Select(attrs={"class": "form-control"}),
            'procesor': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the Processor Model .. eg:- Intel i5-10500H"}),
            'condition': forms.Select(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control", "placeholder": "Without spaces or any symbols or letters"}),
            'tel': forms.TextInput(attrs={"class": "form-control", "placeholder": "Without any symbols or letters"}),
            'city': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the nearest city"}),
            'address': forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the address"}),
        }

        labels = {
            'title': _('Ad Title'),
            'type': _('Laptop Type'),
            'brand': _('Laptop Brand'),
            'model': _('Laptop Model'),
            'category': _('Laptop Category'),
            'year': _('Manufacture Year'),

            'ram': _('Ram of the Laptop(in GB)'),
            'procesor': _('Proccessor of Laptop'),
            'image1': _('Ad Main Image'),
            # 'image2': _('Ad Image'),
            # 'image3': _('Ad Image 2'),
            # 'image4': _('Ad Image 3'),
            # 'image5': _('Ad Image 4'),
            'description': _('Description About the Laptop'),
            'condition': _('Condition'),
            'price': _('Your Price for the Laptop'),
            'tel': _('Your Telephone Number'),
            'city': _('Nearest City'),
            'address': _('Address'),
        }


Manuf_Choices = [
    ('Apple', 'Apple'),
    ('Microsoft', 'Microsoft'),
    ('HP', 'HP'),
    ('Lenovo', 'Lenovo'),
    ('Toshiba', 'Toshiba'),
    ('Dell', 'Dell'),
    ('Samsung', 'Samsung'),
    ('Notepad', 'Notepad'),
    ('MSI', 'MSI'),
    ('Google', 'Google'),

]


Condition_Choices = [
    ('Brand New', 'Brand New'),
    ('Like New', 'Like New'),
    ('Excellent', 'Excellent'),
    ('Good', 'Good'),
    ('Fair', 'Fair'),
    ('Salvage', 'Salvage'),
]


ssd_Choices = [
    ('0', '0'),
    ('128', '128'),
    ('256', '256'),
    ('512', '512'),
    ('1000', '1000'),
    ('2000', '2000'),
    ('3000', '3000'),

]

screen_choices = [
    ('1', 'Yes'),
    ('0', 'No'),
]

ips_choices = [
    ('1', 'Yes'),
    ('0', 'No'),
]

type_Choices = [
    ('Notebook', 'Notebook'),
    ('Ultrabook', 'Ultrabook'),
    ('Gaming', 'Gaming'),
    ('2 in 1', '2 in 1'),
]

screen_Choices = [
    ('11.6', '11.6'),
    ('13', '13'),
    ('13.3', '13.3'),
    ('14', '14'),
    ('15.6', '15.6'),
    ('16', '16'),
    ('17', '17'),
]

brand_Choices = [
    ('Apple', 'Apple'),
    ('HP', 'HP'),
    ('Dell', 'Dell'),
    ('Google', 'Google'),
    ('Lenovo', 'Lenovo'),
    ('Toshiba', 'Toshiba'),
    ('MSI', 'MSI'),
    ('Asus', 'Asus'),
    ('Acer', 'Acer'),
]

gpu_Choices = [
    ('Nvidia', 'Nvidia'),
    ('Intel', 'Intel'),
    ('AMD', 'AMD'),
]
OS_Choices = [
    ('Windows', 'Windows'),
    ('Mac', 'Mac'),
    ('Others/No OS/Linux', 'Others/No OS/Linux'),
]

res_choices = [
    ('1366x768', '1366x768 - HD'),
    ('1920x1080', '1920x1080 - FHD'),
    ('2304x1440', '2304x1440 - Retina'),
    ('2560x1440', '2560x1440 - QHD 2K '),
    ('3840x2160', '3840×2160 - UHD 4K'),

]
cpu_Choices = [
    ('Intel Core i3', 'Intel Core i3'),
    ('Intel Core i5', 'Intel Core i5'),
    ('Intel Core i7', 'Intel Core i7'),
    ('AMD Processor', 'AMD Processor'),
    ('Other Intel Processor', 'Other Intel Processor'),
]

hdd_Choices = [tuple([x, x]) for x in range(0, 1000)]


class PredictForm(forms.Form):
    company = forms.CharField(
        label='Brand/Manufacturer', widget=forms.Select(choices=brand_Choices))
    cpu = forms.CharField(
        label='Processor', widget=forms.Select(choices=cpu_Choices))
    type = forms.CharField(
        label='Type', widget=forms.Select(choices=type_Choices))
    ram = forms.CharField(label='RAM (in GB)')
    weight = forms.CharField(label='Weight in KG')
    touchscreen = forms.CharField(
        label='Touch Screen', widget=forms.Select(choices=ips_choices))
    screensize = forms.CharField(
        label='Screen Size (Inches)', widget=forms.Select(choices=screen_Choices))
    hdd = forms.CharField(
        label='HDD in GB', widget=forms.Select(choices=ssd_Choices))
    ssd = forms.CharField(
        label='SDD in GB', widget=forms.Select(choices=ssd_Choices))
    gpu = forms.CharField(
        label='GPU', widget=forms.Select(choices=gpu_Choices))
    os = forms.CharField(label='OS', widget=forms.Select(choices=OS_Choices))
    ips = forms.CharField(
        label='IPS', widget=forms.Select(choices=ips_choices))
    resolution = forms.CharField(
        label='Resolution', widget=forms.Select(choices=res_choices))
