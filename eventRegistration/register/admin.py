from django.contrib import admin
from .models import EventRegistration
# Register your models here.

#REGISTERING EVENT REGISTRATION MODEL TO DJANGO-ADMIN
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("registrationNo", "registrationDate", "fullname", 'registrationType')
    search_fields = ['registrationType', 'registrationNo']
    
    #VIEW FOR HANDLING CHART.JS
    def changelist_view(self, request, extra_context=None):
        CountEachType = []
        EachType = ['Self', 'Group', 'Corporate', 'Others']
        for typereg in EachType:
            CountEachType.append(len(EventRegistration.objects.filter(
                registrationType = typereg
            )))
        
        extra_context = {"chart_data": CountEachType}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)
    
        
        
admin.site.register(EventRegistration, EventRegistrationAdmin)