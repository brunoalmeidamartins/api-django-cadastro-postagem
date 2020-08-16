from ..models import Postagem
from django.http import Http404

def listar_postagens():
    postagens = Postagem.objects.all()
    return postagens

def cadastrar_postagem(postagem):
    return Postagem.objects.create(titulo=postagem.titulo, descricao=postagem.descricao,
                            url_imagem=postagem.url_imagem)

def listar_postagem_id(id):
    try:
        return Postagem.objects.get(id=id)
    except Postagem.DoesNotExist:
        raise Http404

def editar_postagem(postagem_antiga, postagem_nova):
    postagem_antiga.titulo = postagem_nova.titulo
    postagem_antiga.descricao = postagem_nova.descricao
    postagem_antiga.url_imagem = postagem_nova.url_imagem
    postagem_antiga.save(force_update=True)

def remover_postagem(postagem):
    postagem.delete()
