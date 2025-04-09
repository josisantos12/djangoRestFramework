from django.test import TestCase
from .serializers import LivroSerializer
from .models import Livro

class LivroSerializerTestCase(TestCase):
    def setUp(self):
        self.livro_data = {'titulo': 'Exemplo de Livro', 'autor': 'Autor Teste', 'preco': 100.0}
        self.serializer = LivroSerializer(data=self.livro_data)
        
        # Criar instância de Livro para testes adicionais
        self.livro = Livro.objects.create(
            titulo="Django para Iniciantes",
            autor="Josiane Silva",
            preco=120.0,
            isbn="1234567890123",
            publicado_em="2025-04-02"
        )

    def test_valid_serializer(self):
        """Teste de validação válida do serializer"""
        self.assertTrue(self.serializer.is_valid())

    def test_invalid_serializer(self):
        """Teste de validação inválida do serializer"""
        self.livro_data['preco'] = 'valor_invalido'
        serializer = LivroSerializer(data=self.livro_data)
        self.assertFalse(serializer.is_valid())

    def test_livro_instance_created(self):
        """Teste para verificar a criação de instâncias do modelo"""
        self.assertEqual(str(self.livro), "Django para Iniciantes")