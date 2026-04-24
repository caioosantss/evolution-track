class registrador():

    ferramentas = {}
    funcionarios = {}
    setores = []
    
    @classmethod
    def Registrar_setor(cls):
        setor = input("qual setor deseja registrar? ")
        registrador.setores.append(setor)  
        return (f"setor {setor} registrado")                                

    @classmethod
    def criar_ferramenta(cls):
        print("deseja criar uma ferramenta a qual setor? ")
        print(registrador.setores)
        #incluir uma chamada a classe de ativos para criação da ferramenta
     
    @classmethod   
    def verificar_responsavel(cls):
        print(f"qual responsavel deseja desginar? ")
        print(registrador.funcionarios)
        #montar lógica de case para retornar apenas funcionarios que ja existam em registrador


class ativo():
    def __init__(self,nome,setor):
        self.nome = nome
        self.setor = setor
        self.marca = None
        self.segmento = None

class mala ():
    def __init__(self, ferramental):
        self.responsavel = registrador.verificar_responsavel()
        self.ferramental = ferramental

    def extrair_ferramentas(self):
        #montar lógica apra extrair lista de mala de ferramentas
        #montar lógica consistente pois extrair ferramentas sempre será chamado para a criação de uma mala de ferramentas
        pass    

    