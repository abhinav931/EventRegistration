from django.shortcuts import render, redirect
from .models import EventRegistration
from .forms import RegistrationForm
from django.contrib import messages
import os
from django.http import JsonResponse

countAllPreviousRows = len(EventRegistration.objects.all())

# Create your views here.

#VIEW HANDLING REGISTRATION FORM STARTS HERE
def Registration(request):
    
    if request.method == 'POST':
        
        form = RegistrationForm(request.POST,  request.FILES)
        
        #CHECKING DUPLICACY OF EMAIL
        if EventRegistration.objects.filter(email = request.POST['emailId']).exists():
            messages.error(request, 'email already in use')
            context = {'form': form}
            return render(request, 'index.html', context)
        
        #CHECKING EXTENSIONS VALIDITY
        file_extension = os.path.splitext(request.FILES['idCard'].name)[1]
        
        if not( (file_extension == '.png' and file_extension != '.jpg') or (file_extension != '.png' and file_extension == '.jpg')):
            messages.info(request, f'only .png or .jpg extensions are allowed\n you provided {file_extension}')
            context = {'form': form}
            return render(request, 'index.html', context)
        
        else:
            global countAllPreviousRows
            countAllPreviousRows = len(EventRegistration.objects.all())
            
            newRequest = EventRegistration(fullname = request.POST['fullname'].title(), email = request.POST['emailId'], mobileNumber = request.POST['mobileNumber'], idCard = request.FILES['idCard'], numberOfTickets = request.POST['numberOfTickets'], registrationType = request.POST['registrationType'])
            
            newRequest.save()
            
            #SETTING REGISTRATION NO
            """
            FORMAT = #eventMember_(fullname)_AUTO-GENERATED-UNIQUE-ID
            AUTO-GENERATED-UNIQUE-ID BRINGS UNIQUENESS IN REGISTRATION IDS
            """
            obj = EventRegistration.objects.get(email = request.POST['emailId'])
            obj.registrationNo = '#eventMember_' + '(' +str(obj.fullname) + ')_' + str(obj.id)
            registerId = obj.registrationNo
            fullname = obj.fullname
            
            obj.save()
            
            context = {'fullname': fullname, 'registerId': registerId}
            
            return render(request, 'success.html', context)
        
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    
    return render(request, 'index.html', context)
 
#VIEW HANDLING SUCCESS PAGE
def Success(request):
    return render(request, 'success.html')

#VIEW HANDLING AJAX CALL AT EVERY 3 SECONDS
def UpdateTables(request):
    global countAllPreviousRows
    tableData = len(EventRegistration.objects.all())
    newRecord = False
    if tableData > countAllPreviousRows:
        nameOfNewRecord = EventRegistration.objects.latest('id');
        countAllPreviousRows = tableData
        newRecord = True 
        regId = nameOfNewRecord.registrationNo
        regType = nameOfNewRecord.registrationType
    
    data = {
        'lengthData': tableData,
        'newRecord': newRecord,
        'regId': regId,
        'regType': regType
    }
    return JsonResponse(data)


