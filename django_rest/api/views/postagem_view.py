from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from ..services import postagem_service
from .. serializers import postagem_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import postagem
from ..pagination import PaginacaoCustomizada

class PostagemList(APIView):
    def get(self, request, format=None):
        paginacao = PaginacaoCustomizada()
        postagens = postagem_service.listar_postagens()
        resultado = paginacao.paginate_queryset(postagens, request)
        serializer = postagem_serializer.PostagemSerializer(resultado,context={'request':request},
                                                            many=True)
        return paginacao.get_paginated_response(serializer.data,)
    
    def post(self, request, format=None):
        serializer = postagem_serializer.PostagemSerializer(data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            url_imagem = serializer.validated_data['url_imagem']
            postagem_nova = postagem.Postagem(titulo=titulo, descricao=descricao, 
                                              url_imagem=url_imagem)
            postagem_bd = postagem_service.cadastrar_postagem(postagem_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostagemDetalhes(APIView):
    def get(self, request, id, format=None):
        postagem = postagem_service.listar_postagem_id(id)
        serializer = postagem_serializer.PostagemSerializer(postagem)
        return Response(serializer.data, status.HTTP_200_OK) 
    
    def put(self, request, id, format=None):
        postagem_antiga = postagem_service.listar_postagem_id(id)
        serializer = postagem_serializer.PostagemSerializer(postagem_antiga, data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            url_imagem = serializer.validated_data['url_imagem']
            postagem_nova = postagem.Postagem(titulo=titulo, descricao=descricao,
                                              url_imagem=url_imagem)
            postagem_service.editar_postagem(postagem_antiga, postagem_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        postagem = postagem_service.listar_postagem_id(id)
        postagem_service.remover_postagem(postagem)
        return Response(status=status.HTTP_204_NO_CONTENT)

            




