from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    email = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def _str_(self):
        return self.name


class Notes(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=1000)

    def _str_(self):
        return self.note_text
