from django.shortcuts import render
from django.shortcuts import render
from ml_model.test import predictDisease

# Create your views here.

def index_view(request):
    return render(request, 'ayurveda_app/index.html')

def faq_view(request):
    return render(request, 'ayurveda_app/faq.html')
def aboutus(request):
    return render(request, 'ayurveda_app/aboutus.html')
def contactus(request):
    return render(request, 'ayurveda_app/contactus.html')
def practitioner(request):
    return render(request, 'ayurveda_app/practitioner.html')
def patient(request):
   if request.method=='POST':
       symptoms=request.POST.get('sumptoms')
       predicted_disease=predictDisease(symptoms)
   return render(request, 'ayurveda_app/Patient.html',{'result': predicted_disease})
def prakriti(request):
    return render(request, 'ayurveda_app/prakriti.html')
