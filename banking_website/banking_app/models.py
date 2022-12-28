from django.db import models


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Branch(models.Model):
    programming = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Create your models here.
