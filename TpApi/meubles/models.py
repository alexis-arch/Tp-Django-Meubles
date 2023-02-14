from django.db import models
from django.core.exceptions import ValidationError



class Magasin (models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=100)
    dirigeant = models.CharField(max_length=100)
    CA = models.CharField(max_length=30)

# class Meuble(models.Model):
#     ETAT = [
#         ('NEUF', 'Neuf'),
#         ('OCCASION', 'Occasion'),
#         ('MAUVAIS ETAT', 'Mauvais Etat'),
#         ('INUTILISABLE', 'Inutilisable'),
#     ]
#     STATUT= [
#         ('LIBRE','Libre'),
#         ('VENDU', 'Vendu'),
#     ]
#     nom = models.CharField(max_length=30)
#     etat = models.CharField(max_length=15, default='NEUF', choices=ETAT)
#     statut = models.CharField(max_length=10, default='UND', choices=STATUT)
#     lieu_stockage = models.ForeignKey(Magasin, on_delete=models.PROTECT)
    # image = models.ImageField(upload_to='meubles/', blank=True, null=True)

class Meuble(models.Model):
    ETAT = [
        ('NEUF', 'Neuf'),
        ('OCCASION', 'Occasion'),
        ('MAUVAIS ETAT', 'Mauvais Etat'),
        ('INUTILISABLE', 'Inutilisable'),
    ]
    STATUT = [
        ('LIBRE', 'Libre'),
        ('VENDU', 'Vendu'),
    ]
    nom = models.CharField(max_length=30)
    etat = models.CharField(max_length=15, default='NEUF', choices=ETAT)
    statut = models.CharField(max_length=10, default='UND', choices=STATUT)
    lieu_stockage = models.ForeignKey(Magasin, on_delete=models.PROTECT)

    def clean(self):
        if self.statut == 'VENDU' and self.etat == 'INUTILISABLE':
            raise ValidationError("Un meuble inutilisable ne peut pas être vendu.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Dirigeant (models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)



