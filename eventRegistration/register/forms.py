from django import forms
from django.core.validators import FileExtensionValidator
REGISTRATION_TYPE_CHOICES = [
    ('Self', 'Self'),
    ('Group', 'Group'),
    ('Corporate', 'Corporate'),
    ('Others', 'Others'),
]

#FORM FOR EVENT REGISTRATION MODEL
class RegistrationForm(forms.Form):
    fullname = forms.CharField(max_length = 40,
                               widget = forms.TextInput(attrs = {
                                   'name':'fullname',
                                   'type':'text',
                                   'class': 'form-control',
                                   'id': 'fullname',
                                   'placeholder': 'Enter your full name'
                               })) 
    emailId = forms.EmailField(widget = forms.EmailInput(attrs = {
                                    'name':'email',
                                    'type':"email",
                                    'class':"form-control",
                                    'placeholder':"Enter email",
                                    'id':"email",
                               }))
    mobileNumber = forms.IntegerField(widget = forms.NumberInput(attrs = {
                                   'type':"number",
                                   'class': "form-control",
                                   'placeholder':"Enter mobile no.",
                                   'id':"mobilenumber",
                               }))
    idCard = forms.ImageField()
    numberOfTickets = forms.IntegerField(required = False, widget = forms.NumberInput(attrs = {
                                   'type':"number",
                                   'class': "form-control",
                                   'placeholder':"Enter number of tickets",
                                   'id':"tickets",
                                   'value': '1'
                               }))
    registrationType = forms.CharField(widget=forms.RadioSelect(choices=REGISTRATION_TYPE_CHOICES, attrs = {
        'id': 'registrationtype'
    }))
    

    
    