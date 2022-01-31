import imp
from unicodedata import name
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *


# Homepage
def clinic(request) :
    patients = Patients.objects.all


    # search by name
    if request.method == 'POST':
        if 'search' in request.POST:
            search = request.POST.get('search','')
            print(search)
            patients = Patients.objects.filter(name__icontains = search)
            
    return render(request, 'Interfaces/Clinic.html',{"patients" : patients})

# Add new patient
def addpatient(request) :
    return render(request,'Interfaces/Add-Patient.html')

# Save to database
def addpatientdetails(request):
    if request.method == 'POST':
        if 'name'in request.POST:
            name = request.POST.get('name','')
        else :
            error = True

        if 'bdate'in request.POST:
            bdate = request.POST.get('bdate','')
        else :
            error = True

        if 'contactno'in request.POST:
            contactno = request.POST.get('contactno','')
        else :
            error = True
        
        # Upload image to database
        if len(request.FILES) != 0 :
            print(" image pa")
            image = request.FILES['image']

     
        else :
            error = True

        if 'prescription'in request.POST:
            prescription = request.POST.get('prescription','')
        else :
            error = True
        
        if 'date'in request.POST:
            date = request.POST.get('date','')
        else :
            error = True
        
        if 'bill'in request.POST:
            bill = request.POST.get('bill','')
        else :
            error = True
        
        
        patient = Patients(name = name, dateOFBirth = bdate, contactnumber = contactno, prescription = prescription, date = date,bill = bill,image = image)
        patient.save()

        return redirect('clinic')

# Add New prescription

def addforprescription(request,pk):
    patients = Patients.objects.get(id=pk)

    return render(request, 'Interfaces/Add-Presription.html',{'patients' : patients})

def addprescription(request):
   
    # save to database
    if request.method == 'POST':
        if 'name'in request.POST:
            name = request.POST.get('name','')
        else :
            error = True

        if 'bdate'in request.POST:
            bdate = request.POST.get('bdate','')
        else :
            error = True

        if 'contactno'in request.POST:
            contactno = request.POST.get('contactno','')
        else :
            error = True
        

        

        if 'newprescription'in request.POST:
            newprescription = request.POST.get('newprescription','')
        else :
            error = True
        
        if 'newdate'in request.POST:
            newdate = request.POST.get('newdate','')
        else :
            error = True
        
        if 'newbill'in request.POST:
            newbill = request.POST.get('newbill','')
        else :
            error = True

        patient = Patients(name = name, dateOFBirth = bdate, contactnumber = contactno, prescription = newprescription, date = newdate,bill = newbill)
        patient.save()

    return redirect('clinic')

