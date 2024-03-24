from django.db import models

class BiologyTopic(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='biology/images/')

    def __str__(self):
        return self.title

class BiologyContent(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='biology/content-images/')
    content=models.TextField()

    def __str__(self):
        return self.title