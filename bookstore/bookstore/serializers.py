from rest_framework import serializers
from .models import Livro  # Substitua pelo nome do seu modelo

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'  # Para incluir todos os campos do modelo