from django.db import models

class PhysicsTopic(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='physics/images/')

    def __str__(self):
        return self.title
    
class PhysicsContent(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='physics/content-images/')
    content=models.TextField()

    def __str__(self):
        return self.title