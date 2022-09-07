from django.db import models
# Create your models here.


class Responces(models.Model):
    name = models.TextField(null=False)
    email = models.TextField()
    comment = models.TextField(null=False)
    createdAt = models.DateTimeField()
