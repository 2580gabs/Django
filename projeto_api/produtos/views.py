from django.shortcuts import render # type: ignore
from django.shortcuts import render  # type: ignore
from rest_framework import generics  # type: ignore
from .models import Categoria, Produto 
from .serializers import CategoriaSerializer, ProdutoSerializer 
class CategoriaList(generics.ListCreateAPIView): 
 queryset = Categoria.objects.all() 
 serializer_class = CategoriaSerializer





class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):  
  queryset = Categoria.objects.all() 
  serializer_class = CategoriaSerializer 
class ProdutoList(generics.ListCreateAPIView): 
  queryset = Produto.objects.all() 
  serializer_class = ProdutoSerializer 
class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):  queryset = Produto.objects.all() 
serializer_class = ProdutoSerializer






# Create your views here.
