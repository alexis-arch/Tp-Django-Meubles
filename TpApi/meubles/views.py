from django.shortcuts import render
from .models import Meuble, Magasin, Dirigeant
from .serializer import MeubleSerializer, MagasinSerializer, DirigeantSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# from rest_framework.permission import IsAuthenticated
from .permissions import IsAdminAuthentificated


# Create your views here.

class MeubleViewset(ModelViewSet):
    serializer_class = MeubleSerializer
    # admin_classes = IsAdminAuthentificated
    permission_classes = [IsAdminAuthentificated]

    def get_queryset(self):
        queryset = Meuble.objects.all()

        return queryset

class MagasinViewset(ModelViewSet):
    serializer_class = MagasinSerializer
    permission_classes = [IsAdminAuthentificated]

    def get_queryset(self):
        queryset = Magasin.objects.all()
        return queryset
        
class DirigeantViewset(ModelViewSet):
    serializer_class = DirigeantSerializer
    permission_classes = [IsAdminAuthentificated]

    def get_queryset(self):
        queryset = Dirigeant.objects.all()
        return queryset