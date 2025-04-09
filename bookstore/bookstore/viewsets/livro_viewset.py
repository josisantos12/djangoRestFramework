from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from bookstore.models import Livro
from bookstore.serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    authentication_classes = [TokenAuthentication]  # Habilita autenticação baseada em token
    permission_classes = [IsAuthenticated]            # Exige que o usuário esteja autenticado