from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    intelligent = models.CharField(max_length=300)
    image = models.ImageField(null=True, upload_to='projects/')

    def __str__(self):
        return self.title
