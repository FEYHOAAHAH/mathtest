from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=255)
    difficulty = models.CharField(max_length=10, choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')])
    correct_answer = models.IntegerField()
    option1 = models.IntegerField()
    option2 = models.IntegerField()
    option3 = models.IntegerField()
    option4 = models.IntegerField()