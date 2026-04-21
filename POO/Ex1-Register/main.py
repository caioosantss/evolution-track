class Registro:
    """Classe para gerenciar o catálogo de artistas e suas músicas."""
    Artistas = []
    idArtistas = 0
    musicas = []


    def __init__(self):
        self.nome = None
        self.idartista = Registro.idArtistas

        self.discografia = []

  
    def __str__(self):
        return (
        f"o artista {self.nome} é o artista numero {self.idartista} e possui as seguintes músicas em sua discografia {self.discografia}"
        )


    def Registrar_artista(self,nome):
        #verifica se o artista ja esta cadastrado
        for item in Registro.Artistas:

            if item.nome == nome:

                print(f"artista {item.nome} ja cadastrado no ID {item.idartista} ")
                return item
            #caso esteja retorna o item, ou seja retorna true
        self.nome = nome
        Registro.Artistas.append(self)
        print(f"o artista {nome} acaba de ser registrado")
        return False
            #caso não esteja, adiciona o item a lista de objetos e retorna false
                    
    def Adicionar_Musica(self,disco):

            if disco not in self.discografia:

                self.discografia.append(disco)
                Registro.musicas.append(disco)
                print("musica adicionada")
                return False

            if disco in self.discografia:
                print(f"musica {disco} ja adicionada na discografia no id {Registro.musicas[ID]}")
                return False
  
          
    def Criar_ID(self):

            Registro.idArtistas += 1
            self.idartista = Registro.idArtistas
            print(f"ID para o artista {self.nome} criado. ID Nº {self.idartista}")


            return ('id criado')
        
if __name__ == "__main__":

    while True:

        artista = Registro()


        nome = artista.Registrar_artista(input("qual o nome do artista? ").lower())  
    
        if nome is not False:
         #rota caso o artista já exista e vamos utlizar um ja existente
            artista = nome
           


            musica = artista.Adicionar_Musica(input("qual musica deseja adcionar? ").lower())
            print(artista.discografia)


        elif nome is False:
            #rota caso o artista seja cadastrado
            artista.Criar_ID()
            musica = artista.Adicionar_Musica(input("qual musica deseja adcionar? ").lower())
            print(artista.discografia)


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
        
       
    