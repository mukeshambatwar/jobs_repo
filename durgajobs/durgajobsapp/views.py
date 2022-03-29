from django.shortcuts import render
from durgajobsapp.models import Hydrabadjobs,Punejobs,Banglorjobs
# Create your views here.
def homepage_view(request):
    return render(request,'jobsapp/index.html')
    
def Hydrabadjobs_view(request):
    jobs_list=Hydrabadjobs.objects.all()  #it fetch all the records from the database
    my_dict={'jobs_list':jobs_list}
    return render(request,'jobsapp/Hydrabadjobs.html',context=my_dict)
