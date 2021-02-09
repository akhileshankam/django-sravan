from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=500)
    subject = models.CharField(max_length=5000)
    def __str__(self):
        return self.name
class resume(models.Model):
    name=models.CharField(default=1,max_length=50)
    resume=models.FileField(blank=True)
    def __str__(self):
        return self.name
