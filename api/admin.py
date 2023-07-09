from django.contrib import admin
from .models import Bus,Users,Pharmacies,Admin
# Register your models here.
 
admin.site.register(Users)
admin.site.register(Bus)
admin.site.register(Pharmacies)
admin.site.register(Admin)