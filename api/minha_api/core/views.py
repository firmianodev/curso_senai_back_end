from django.shortcuts import render

from .filters import ProdutoFilter
from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from .models import Produto
from .serializers import ProdutoSerializaer

# class ProdutoListView(APIView):
#     def get(self, request):
#         produtos = Produto.objects.all()
#         s = ProdutoSerializer(produtos, many=True)
#         return Response(s.data)
    
#     def post(self, request):
#         s = ProdutoSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data, status=201)
#         return Response(s.erros, status=400)
    
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializaer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProdutoFilter
    search_fields = ['nome']
    ordering_fields = ['preco', 'nome']