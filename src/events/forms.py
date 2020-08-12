from django.contrib.auth.forms import UserCreationForm
from events.models import User, HappeningEvents
from django import forms
from django.contrib.admin import widgets

class SignUpForm(UserCreationForm):  
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput())
    interests = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your interests in comma separated form. Like Party, Trekking, Reunion, etc'}))
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'age',
            'institution',
            'interests',
            'address'
        )


class OrganizeEvent(forms.ModelForm):
    description = forms.CharField(max_length=4096, widget=forms.TextInput(attrs={'placeholder': 'Describe your event in detail', 'rows': 6}))
    event_date = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Format: DD/MM/YY'}))
    event_type = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter event Type in comma separated form like Party, Adventure, Nightout, Trip etc'}))

    class Meta:
        model = HappeningEvents


        fields = (
            'name',
            'poster',
            'address',
            'event_date',
            'contact_number',
            'event_type',
            'description',
        )