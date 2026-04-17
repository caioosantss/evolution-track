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
    def Registrar_artista(cls):

            artista = input("digite o nome do artista ")
            if artista not in Registro.Artista:
                Registro.Artistas.append(artista)
            else:
                #achar formas de incluir o ID
                return ("artista ja registrado")

    def Adicionar_Musica(self,musica):
        if musica not in self.discografia:
            self.discografia = musica
        else:
            return ("musica ja esta na discografia")
