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

    def Verifica_musica (self, musica):
        if musica not in Registro.musicas:
            return True
        else:
            return False 

    def Incluir_Musica(self,musica):
        if musica not in self.discografia:
            self.discografia = musica

    @classmethod    
    def Verifica_artista (cls, artista):
        if artista not in Registro.Artistas:
            return True
        else:
            return False


    @classmethod
    def Registrar_artista(cls):
        #inicia fabrica de objetos

            #registra o artista e uma musica
            nome = input("digite o nome do artista ")
            if Registro.Verifica_artista(nome) is True:
                artista = nome

                #inicia cadastro de musica
                musica = input("digite uma musica ")
                
                if Registro.Verifica_musica(musica) is True:
                    
                    Registro.Incluir_Musica(musica)
                    return(artista)

                else:
  
                   return('musica ja incluida na discografia do artista')
            else:
                #incluir aqui uma forma de introduzir o ID do artista
                return("artista já registrado")

    def Incluir_Musica(self,musica):
        if musica not in self.discografia:
            self.discografia = musica
