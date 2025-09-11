from django.contrib import admin
from .models import drive
from .models import hire
class driveadmin(admin.ModelAdmin):
    data=('name','fathername','age','religion','city','nearbylocation ','experience ','mobile','alternate_mobile','address','permanent_address','dlnumber','transport','aadhar','pan' ,'uploadpan','uploadaadhar','resume')

admin.site.register(drive,driveadmin)
class hireadmin(admin.ModelAdmin):
    data2=('id','name','fathername','religion','city','nearbylocation','alternate_mobile','transport','aadhar','pan','uploadpan','uploadaadhar')
admin.site.register(hire,hireadmin)


