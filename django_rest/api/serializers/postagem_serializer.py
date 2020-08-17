from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Postagem

class PostagemSerializer(serializers.ModelSerializer):
    #links = serializers.SerializerMethodField()
    class Meta:
        model = Postagem
        fields = ('id', 'titulo', 'descricao', 'url_imagem',)
    '''
    def get_links(self, obj):
        request = self.context['request']
        return {
            'self': reverse('postagem-detalhes', kwargs={'id':obj.pk}, request=request),
            'delete': reverse('postagem-detalhes', kwargs={'id':obj.pk}, request=request),
            'update': reverse('postagem-detalhes', kwargs={'id':obj.pk}, request=request),
            
        }
    '''
    