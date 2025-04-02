from django.test import TestCase
from .serializers import LivroSerializer

class LivroSerializerTestCase(TestCase):
    def setUp(self):
        self.livro_data = {'titulo': 'Exemplo de Livro', 'autor': 'Autor Teste', 'preco': 100.0}
        self.serializer_data = LivroSerializer(data=self.livro_data)

    def test_valid_serializer(self):
        self.assertTrue(self.serializer_data.is_valid())

    def test_invalid_serializer(self):
        self.livro_data['preco'] = 'valor_invalido'
        serializer = LivroSerializer(data=self.livro_data)
        self.assertFalse(serializer.is_valid())

from bookstore.models import Livro
livro = Livro(titulo="Django para Iniciantes", autor="Josiane Silva", isbn="1234567890123", publicado_em="2025-04-02")
livro.save()
print(livro)