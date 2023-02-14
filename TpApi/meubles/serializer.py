from rest_framework.serializers import ModelSerializer
from .models import Meuble, Magasin, Dirigeant


class MeubleSerializer(ModelSerializer):
    class Meta:
        model= Meuble
        fields = ['id', 'nom', 'etat', 'statut', 'lieu_stockage']

class MagasinSerializer(ModelSerializer):
    class Meta:
        model = Magasin
        fields = ['nom', 'adresse', 'dirigeant', 'CA']

class DirigeantSerializer(ModelSerializer):
    class Meta:
        model = Dirigeant
        fields = ['id', 'nom', 'prenom']

