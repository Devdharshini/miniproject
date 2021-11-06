from django.db import models

# Create your models here.

class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)

    @staticmethod
    def get_counter_by_name(name):
        return login.objects.filter(username = name)