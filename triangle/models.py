from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Log(models.Model):
    path = models.CharField(max_length=30)
    method = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.path
