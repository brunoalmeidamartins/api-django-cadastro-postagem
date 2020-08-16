from django.urls import path, include
from .views import postagem_view, usuario_view

urlpatterns = [
    path('postagens/', postagem_view.PostagemList.as_view(), name='postagem-list'),
    path('postagens/<int:id>', postagem_view.PostagemDetalhes.as_view(), name='postagem-detalhes'),
    path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario-list'),
]
