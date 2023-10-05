from django.db import models
from django.contrib import auth

# Create your models here.
class Account(models.Model):
    Identity = (
    	('resident','住戶'),
    	('non-resident','非住戶'),
    	('landlord','房東'),
    )

    name = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    identity = models.CharField(max_length=20, choices=Identity, default=Identity[0][1])
    def __str__(self):
    	return self.name.username

# class Account_1(models.Model):
#     Identity = (
#     	('resident','住戶'),
#     	('non-resident','非住戶'),
#     	('landlord','房東'),
#     )
#     identity = models.CharField(max_length=20, choices=Identity, default=Identity[0][1])
#     def __str__(self):
#     	return self.name.username


class Room(models.Model):
    roomnumber = models.CharField(max_length = 10,null =False)
    detail = models.TextField()
    rent = models.PositiveIntegerField(null = True,blank =True)
    enable = models.BooleanField(default = False)
    def __str__(self):
        return self.roomnumber

class Resident(models.Model):
    name = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    default_room = Room.objects.get(roomnumber = "公共區域")
    roomnumber = models.ForeignKey(Room, on_delete= models.CASCADE,default = Room.objects.get(roomnumber = default_room).pk)
    phone_number = models.CharField(max_length=15, null=False)
    address = models.CharField(max_length=20, null=False)
    date_start = models.DateField(null = True,blank =True)
    date_end = models.DateField(null = True,blank =True)
    emergencycontact=models.CharField(max_length=20, null=False) #緊急聯絡人
    emergencynumber=models.CharField(max_length=20, null=False) #緊急聯絡電話
    enable = models.BooleanField(default = False)
    def __str__(self):
    	return self.name.username

class Book(models.Model):
    time = models.DateTimeField()
    phone = models.CharField(max_length = 20,null = False)
    name = models.CharField(max_length = 50,null= False)
    message = models.TextField(default="無")
    def __str__(self):
        return self.name

class Question(models.Model):
    roomnumber = models.ForeignKey(Room, on_delete= models.CASCADE)
    name = models.CharField(max_length = 50,null= False)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.roomnumber
class Photo(models.Model):
    roomnumber = models.ForeignKey(Room, on_delete= models.CASCADE,null =False)
    photo =  models.ImageField(upload_to='image/')
    def __str__(self):
        return self.roomnumber.roomnumber

class Electricity_total(models.Model):
    current = models.CharField(max_length = 10,null =False,default="current")
    startdate=models.DateField()
    enddate = models.DateField()
    totaluse=models.PositiveIntegerField()
    totalbill = models.PositiveIntegerField()
    per_price=models.DecimalField(max_digits=10,decimal_places=1)
    def __str__(self):
        return self.current
class Electricity_personal(models.Model):
    roomnumber=models.OneToOneField(Room,on_delete=models.CASCADE)
    last_use = models.DecimalField(max_digits=10,decimal_places=1)
    current_use =models.DecimalField(max_digits=10,decimal_places=1)
    avg_totaluse = models.DecimalField(max_digits=10,decimal_places=1)
    personaluse=models.DecimalField(max_digits=10,decimal_places=1)
    bill = models.DecimalField(max_digits=10,decimal_places=0)
    pay = models.BooleanField(default = False)
    def __str__(self):
        return self.roomnumber.roomnumber