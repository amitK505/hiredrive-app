from django.db import models

class drive(models.Model):
    name=models.CharField(max_length=50)
    fathername=models.CharField(max_length=50)
    age=models.PositiveIntegerField()
    religion=models.CharField(max_length=10)
    city =models.CharField(max_length=10)
    nearbylocation =models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    mobile = models.CharField(max_length=10)
    alternate_mobile =models.CharField(max_length=10)
    address = models.TextField(max_length=500)
    permanent_address =models.TextField(max_length=500)
    dlnumber=models.CharField(max_length=19)
    transport=models.CharField(max_length=50)
    aadhar=models.CharField(max_length=12)
    pan =models.CharField(max_length=20)
    uploadpan=models.FileField()
    uploadaadhar=models.FileField()
    resume=models.FileField()
class hire(models.Model):
    name=models.CharField(max_length=20)
    fathername=models.CharField(max_length=55)
    religion=models.CharField(max_length=10)
    city =models.CharField(max_length=10)
    nearbylocation =models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    alternate_mobile =models.CharField(max_length=10)
    transport=models.CharField(max_length=50)
    aadhar=models.CharField(max_length=12)
    pan =models.CharField(max_length=20)
    uploadpan=models.FileField()
    uploadaadhar=models.FileField()








