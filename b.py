from django.db import models

class Ask(models.Model):
    ask_text = models.CharField(max_length=100)

class Ask(models.Model):
    ask = models.ForeignKey(Ask)
    answer_text = models.CharField(max_length=100)
    total= models.IntegerField(default=0)