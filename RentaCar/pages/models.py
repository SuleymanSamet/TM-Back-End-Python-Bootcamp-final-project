from django.db import models


class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Phone_Number = models.CharField(max_length=100)
    Massage = models.TextField(blank=True)

    def __str__(self):
        return self.Name
