from django.shortcuts import render


# Create your views here.
def resign_page(request):
    return render(request, 'basic/resign_page.html')

def crate_patient(request):
    return render(request, 'basic/crate_patient.html')
