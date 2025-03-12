from django import forms
from .models import Profile
from django.utils.translation import ugettext_lazy as _

class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
        'full_name',
        'address',
        'city',
        'country',
        'tel',
        'you_are',
        'image'
        )

        widgets = {
        'full_name':forms.TextInput(attrs={"class":"form-control"}),
        'address':forms.TextInput(attrs={"class":"form-control"}),
        'city':forms.TextInput(attrs={"class":"form-control"}),
        'country':forms.TextInput(attrs={"class":"form-control"}),
        'tel':forms.TextInput(attrs={"class":"form-control"}),
        'you_are':forms.TextInput(attrs={"class":"form-control"}),
        }

        labels = {
            'full_name': _('Full Name'),
            'address': _('Address'),
            'city': _('City'),
            'country': _('Country'),
            'tel': _('Telephone Number'),
            'you_are': _('Your Profession'),
            'image': _('Change Profile Picture'),
        }
