from django.db import models

class Technology(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title



# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.ManyToManyField(Technology)
    url = models.URLField(blank=True)
    image = models.FileField(blank=True)
    

    def __str__(self):
        return self.title