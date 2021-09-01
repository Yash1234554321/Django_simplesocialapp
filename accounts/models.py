from django.db import models
from django.contrib import auth#built in model with all auth elements

# Create your models here.
class User(auth.models.User):
    def __str__(self):
        return "@{}".format(self.username)
