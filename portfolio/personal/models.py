from django.db import models

def one_to_houndred_validation(value):
    if value in range(1,101):
        return value
    else:
        raise ValidationError('This is not a percentage')
 


# Create your models here.
class Skill(models.Model):
    skill_name = models.CharField(max_length=100, unique=True)
    percentaga = models.PositiveIntegerField(default=10, validators=[one_to_houndred_validation])


class Education(models.Model):
    title = models.CharField(max_length=200, unique=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)
    university = models.CharField(max_length=255)
    description = models.TextField()


class Work(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=150)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.company}"
    

class SuccessStory(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    work = models.ForeignKey(Work, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']