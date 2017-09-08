from django.db import models


class Team(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    affiliation = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    created_by = models.CharField(max_length=200, unique=True)
    modified_by = models.CharField(max_length=200, unique=True)
    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
