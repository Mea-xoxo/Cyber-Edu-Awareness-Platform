from django.db import models

class Topic(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
    text = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.text
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    text = models.CharField(max_length =255)
    is_correct = models.BooleanField(default = False)
    
    def __str__(self):
        return self.text
    
    

# Create your models here.
