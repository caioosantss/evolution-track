class registrador():

    ferramentas = {}
    funcionarios = []
    setores = []

    def Registrar_setor(self):
        setor = input("qual setor deseja registrar? ")
        registrador.setores.append(setor)  
        return (f"setor {setor} registrado")                                

    @classmethod
    def cria_ferramenta(cls):
        print("deseja criar uma ferramenta a qual setor? ")
        print(registrador.setores)

class ativo():
    def __init__(self,nome,setor):
        self.nome = nome
        self.setor = setor
        self.marca = None
        self.segmento = None

class mala ():
    def __init__(self, ferramental):
        self.responsavel = mala.verificar_responsavel()
        self.ferramental = mala.extrair_ferramentas()

    def verificar_responsavel(self):
        print(f"qual responsavel deseja desginar? ")
        print(registrador.funcionarios)
        #montar lógica de case para retornar funcionarios

    def extrair_ferramentas(self):
        #montar lógica apra extrair lista de mala de ferramentas
        #montar lógica de registro individual de ferramentas pela própria lógica a partir da classe ativos
        pass

    