from django.db import models


# Create your models here.

class kfc(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    @staticmethod
    def get_item_by_id(ids):
        return kfc.objects.filter(id__in = ids)

class Users(models.Model):
    username = models.CharField(max_length=100)
    phone_no = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=8)

    @staticmethod
    def get_customer_by_mail(mail):
        return Users.objects.filter(email = mail) 

class Carts(models.Model):
    item = models.IntegerField()
    quantity = models.IntegerField()
    
    



    