from django.db import models

# Create your models here.

class Pokemon(models.Model):
    pokedex_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=50)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_url = models.URLField()

    type1 = models.CharField(max_length=20, blank=True)
    type2 = models.CharField(max_length=20, blank=True, null=True)

    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['pokedex_number']
    
    def __str__(self):
        return f"#{self.pokedex_number:03d} - {self.name.title()}"
