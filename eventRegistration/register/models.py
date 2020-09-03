from django.db import models
from django.core.validators import validate_email, EmailValidator, FileExtensionValidator
from django.utils import timezone
from django.urls import reverse

# Create your models here.

REGISTRATION_TYPE_CHOICES = [
    ('Self', 'Self'),
    ('Group', 'Group'),
    ('Corporate', 'Corporate'),
    ('Others', 'Others'),
]


#MODEL FOR EVENT REGISTRATION FORM 
class EventRegistration(models.Model):
    registrationDate = models.DateField(default = timezone.now)
    fullname = models.CharField(max_length = 50)
    registrationNo=  models.CharField(max_length = 100, unique = True)
    email = models.EmailField(max_length = 50, validators=[validate_email, EmailValidator])
    mobileNumber = models.IntegerField()
    idCard = models.ImageField(upload_to = 'idUploads/',  validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg'])])
    numberOfTickets = models.IntegerField(default = 1)
    registrationType = models.CharField(choices = REGISTRATION_TYPE_CHOICES, max_length = 20)
    
  
    def __str__(self):
        return self.registrationNo 