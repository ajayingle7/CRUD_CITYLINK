from django.db import models

# Create your models here.

class City(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=50)
    dist = models.CharField(max_length=50)
    state  = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.cid}--{self.cname}--{self.dist}--{self.state}'


class Zip(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    area = models.CharField(max_length=50)
    zip = models.IntegerField()


    def __str__(self):
        return f'{self.city}--{self.area}'