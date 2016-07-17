from django.db import models

class Question(models.Model):
    question=models.CharField(max_length=250)
    #number=models.IntegerField()

    def __str__(self):
        return self.question

# Create your models here.
