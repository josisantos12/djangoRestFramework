from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class LivroViewSetTestCase(APITestCase):
    def setUp(self):
        self.livro_data = {"titulo": "Livro Teste", "autor": "Autor Teste", "preco": 100.0}
        self.livro = Livro.objects.create(**self.livro_data)
        self.url = "/livros/"  # Endpoint do ViewSet

    def test_list_livros(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_livro(self):
        novo_livro = {"titulo": "Novo Livro", "autor": "Novo Autor", "preco": 50.0}
        response = self.client.post(self.url, novo_livro)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_livro(self):
        response = self.client.get(f"{self.url}{self.livro.id}/")  # Requisição para o item específico
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_livro(self):
        update_data = {"titulo": "Livro Atualizado"}
        response = self.client.patch(f"{self.url}{self.livro.id}/", update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_livro(self):
        response = self.client.delete(f"{self.url}{self.livro.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)