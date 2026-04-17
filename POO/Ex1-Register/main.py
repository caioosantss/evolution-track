class Registro:
    """Classe para gerenciar o catálogo de artistas e suas músicas."""
    idMusicas = 0
    Artistas = []
    idArtistas = 1
    musicas = {}

    def __init__(self):
        self.nome = None
        self.idartista = Registro.idArtistas
        self.idMusica = None
        self.discografia = []
        self.Musica = None
  
    def __str__(self):
        return (
        f"o artista {self.nome} é o artista numero {self.idartista} e possui as seguintes músicas em sua discografia {self.discografia}"
        )

    def Registrar_artista(self):

            artista = input("digite o nome do artista ")
            if artista not in Registro.Artistas:
                Registro.Artistas.append(artista)
                self.nome = artista
                print(f'o artista {artista} acaba de ser registrado')
                return artista
            else: 
                #incluir formas de encontrar o ID de artistas já cadastrados
                print(f'o artista {artista} ja foi registrado')  
                for i, artista_da_vez in enumerate(Registro.Artistas):
                    if artista_da_vez == artista:
                        print(f'o artista {artista} ja foi registrado no ID {Registro.Artistas[i]}')
                        return Registro.Artistas[i]
                    
    def Adicionar_Musica(self,musica):
        try:
            if musica not in self.discografia:
                self.discografia = musica
            else:
                return False
        except:
            return musica
          
    def Criar_ID(self):
        try: 
            Registro.idMusicas =+ 1
            self.idMusica = Registro.idMusicas
            print(f"ID para musica {self.Musica} criado. ID Nº {self.idMusica}")
        except:
            return ('id criado')
        
if __name__ == "__main__":

    while True:

        artista = Registro()


        nome = Registro.Registrar_artista(artista)
    
        if nome is not False:
            musica = input("qual musica deseja registrar? ")
            artista.Adicionar_Musica(musica)
        
            if musica is False:
                print("musica ja esta na discografia")
            else:
                artista.Criar_ID()
                print(artista)

            pergunta1 = input("deseja registrar mais musicas? ")


            #pergunta referente a continuidade do registro de artistas    
            pergunta2 = input("deseja continuar? ")
            if pergunta2 == 'n':
                break            
            
        else:
            #incluir busca de ID de todos os artistas para mostrar o ID do artista correspondente
            print("artista ja registrado")
        
       
    