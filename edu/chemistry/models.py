from django.db import models

class ChemistryTopic(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chemistry/images/')

    def __str__(self):
        return self.title
    
class ChemistryContent(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chemistry/content-images/')
    content=models.TextField()

    def __str__(self):
        return self.title