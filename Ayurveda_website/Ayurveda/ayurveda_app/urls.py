from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('faq/', views.faq_view, name='faq'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contactus/',views.contactus,name='contactus'),
    path('practitioner/',views.practitioner,name='practitioner'),
    path('patient/',views.patient,name='patient'),
    path('prakriti/',views.prakriti,name='prakriti')



]
