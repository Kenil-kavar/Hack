from django.shortcuts import render
from django.shortcuts import render
from ml_model.test import predictDisease
import csv
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
       symptoms=request.POST.get('symptoms')
       sym=list(symptoms.split(','))
       predicted_disease=predictDisease(sym)
       print(predicted_disease)
       return render(request, 'ayurveda_app/Result.html',{'result': predicted_disease})
   else  :
       return render(request, 'ayurveda_app/patient.html')

def prakriti(request):
   if request.method=='POST':
       bodySize=request.POST.get('bodySize')
       bodyWeight=request.POST.get('bodyWeight')
       height=request.POST.get('height')
       boneStructure=request.POST.get('boneStructure')
       complexion=request.POST.get('complexion')
       generalFeelOfSkin=request.POST.get('generalFeelOfSkin')
       textureOfSkin=request.POST.get('textureOfSkin')
       hairColor=request.POST.get('hairColor')
       appearanceOfHair=request.POST.get('appearanceOfHair')
       shapeOfFace=request.POST.get('shapeOfFace')
       eyes=request.POST.get('eyes')
       eyelashes=request.POST.get('eyelashes')
       blinkingOfEyes=request.POST.get('blnkingOfEyes')
       cheeks=request.POST.get('cheeks')
       nose=request.POST.get('nose')
       teethAndGums=request.POST.get('teethAndGums')
       lips=request.POST.get('lips')
       nails=request.POST.get('nails')
       appetite=request.POST.get('appetite')
       likingTastes=request.POST.get('likingTastes')
       data=[bodySize, bodyWeight, height, boneStructure,complexion,generalFeelOfSkin, textureOfSkin,hairColor,appearanceOfHair,
             shapeOfFace,eyes,eyelashes,blinkingOfEyes,cheeks,nose,teethAndGums,lips,nails,appetite,likingTastes]

       file_path = 'hifi/dosh/values.csv'
       with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
            print('successful')  # Note the double square brackets here

            return render(request, 'ayurveda_app/prakriti.html',{'data':data})

        # Add any appropriate error handling here

   else  :
       return render(request, 'ayurveda_app/prakriti.html')


def result(request):
    return render(request, 'ayurveda_app/Result.html')
def learn(request):
    return render(request, 'ayurveda_app/learn.html')