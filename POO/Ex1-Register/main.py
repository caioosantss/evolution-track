class Registro:
    """Classe para gerenciar o catálogo de artistas e suas músicas."""
    idMusicas = 0
    Artistas = []
    idArtistas = 0
    musicas = {}
    def __init__(self,artista,Musica,idMusica):
        self.artista = artista
        self.idartista = Registro.idArtistas
        self.idMusica = idMusica
        self.discografia = []
        self.Musica = Musica
  
    def __str__(self):
        return (
        f"o artista {self.artista} é o artista numero {self.idartista} e possui as seguintes músicas em sua discografia {self.discografia}"
        )

    @classmethod
    def Verificar_musica (self,musica):
        if musica not in Registro.Artistas:
            return True
        else:
            return False


    @classmethod    
    def Verifica_artista (self, artista):
        if artista not in Registro.Artistas:
            return True
        else:
            return False


    @classmethod
    def Registrar_artista(cls):
        #inicia fabrica de objetos
            a
        