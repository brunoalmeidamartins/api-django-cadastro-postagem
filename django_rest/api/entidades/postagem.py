class Postagem():
    def __init__(self, titulo, descricao, url_imagem):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__url_imagem = url_imagem

    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def url_imagem(self):
        return self.__url_imagem
    
    @url_imagem.setter
    def url_imagem(self, url_imagem):
        self.__url_imagem = url_imagem