from django.db import models

class PrimaryContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def _str_(self):
        return self.name

class SecondaryContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def _str_(self):
        return self.name
