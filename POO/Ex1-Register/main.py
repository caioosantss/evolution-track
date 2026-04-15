class Register:
    """Classe para gerenciar o catálogo de artistas e suas músicas."""
    idMusicas = 0
    Artistas = []
    idArtistas = 0
    musicas = {}
    def __init__(self,artista,Musica,idMusica):
        self.artista = artista
        self.idartista = Register.idArtistas
        self.idMusica = idMusica
        self.discografia = []
        self.Musica = Musica
  
    def __str__(self):
        return (f"o artista {self.artista} é o artista numero {self.idartista} e possui as seguintes músicas em sua discografia {self.discografia}")
        
    @classmethod
    def Debbut(cls): 
        musica = input("qual o nome da musica? ")

        if musica in Register.musicas:
            return print(f'a musica {musica} ja esta registrada e pertence ao cantor {Register.musicas[musica]}')  
        

        artista = input("qual o nome do artista?")

        if artista not in cls.Artistas:
            cls.Artistas.append(artista)
            cls.idArtistas += 1
            cls.musicas[musica] = artista
            print(f"artista '{artista}' adicionado junto a seu debbut '{musica}'")
            return cls(artista,musica,cls.idMusicas)

    
        cls.musicas[musica] = artista
        cls.idArtistas += 1
        print(f"a musica '{musica}' foi adicionada a sua discografia")
        return cls(musica,artista,cls.idMusicas)
        
    def Discografia(self,musica):
        if musica not in self.discografia:
            self.discografia.append(musica)


if __name__ == "__main__":

    while True:
        art = Register.Debbut()

        art.Discografia(art.Musica)


        while True:

            registrar = input("deseja continuar o registro de musicas?")

            if registrar == 'n':
                Register.Artistas.append(art)
                break
            else:

                art.Musica = input("qual musica deseja registar? ")
                art.Discografia(art.Musica)

                print(art)

        regisART = input("deseja registrar mais um artista? ")

        if regisART == 'n':
            break

for item in Register.Artistas:
    print(item)