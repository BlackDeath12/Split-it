from django.db import models

PRIORITY = [
    ("H" , "High"),
    ("M" , "Medium"),
    ("L" , "Low")
]

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=60)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=1, choices=PRIORITY)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "the question"
        verbose_name_plural = "Users's questions"
