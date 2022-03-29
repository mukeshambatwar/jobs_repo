from django.contrib import admin
from durgajobsapp.models import Punejobs,Banglorjobs,Hydrabadjobs
# Register your models here.

class HydrabadjobsAdmin(admin.ModelAdmin):
    list_display=['date','title','company','eligibility','email','phonenumber','address']

admin.site.register(Hydrabadjobs,HydrabadjobsAdmin)

class PunejobsAdmin(admin.ModelAdmin):
    list_display=['date','title','company','eligibility','email','phonenumber','address']

admin.site.register(Punejobs,PunejobsAdmin)

class BanglorjobsAdmin(admin.ModelAdmin):
    list_display=['date','title','company','eligibility','email','phonenumber','address']

admin.site.register(Banglorjobs,BanglorjobsAdmin)
