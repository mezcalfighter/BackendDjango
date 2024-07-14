from django.db import models

# Create your models here.
class Car(models.Model):
    title = models.TextField(max_length=250)
    model_car = models.TextField(max_length=250, null=True)
    year = models.TextField(max_length=4, null=True)
    color = models.TextField(max_length=10, null=True)

    def __str__(self):
        return f"Model: {self.model_car} \nBrand:{self.title} \nColor:{self.color} \nYear:{self.year}"