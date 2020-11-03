from django.db import models


class Personagem(models.Model):
    name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=20, blank=False)
    school = models.CharField(max_length=100, blank=False)
    house = models.CharField(max_length=100, blank=False)
    patronus = models.CharField(max_length=20, blank=False)

    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE