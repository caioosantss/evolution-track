class registrador():

    ferramentas = {} #ferramentas é um dicionario de objetos
    funcionarios = {} #funcionario é um dicionarios de objetos
    setores = [] #setor é um indíce para buscar ferramentas e funcionarios

    def Registrar_setor(self):
        setor = input("qual setor deseja registrar? ").lower()
        registrador.setores.append(setor)  
        return (f"setor {setor} registrado")                                

    @classmethod
    def cria_ferramenta(cls):
        ferramenta = input("qual ferramenta deseja cadastrar? ").lower()
        
        setor = input("para qual setor deseja designar? ")

        while True:
            if setor not in registrador.setores:
                print("setor invalido")
            else:
                break

        registrador.ferramentas[setor] = ferramenta
        return (f'a ferramenta {ferramenta} registrada com sucesso no setor {setor}')
        

    @classmethod
    def criar_funcionario(cls):
        funcionario = input("qual funcionario deseja cadastrar? ").lower()
        print(setores)
        setor = input("para qual setor deseja designar? ")

        while True:
            if setor not in registrador.setores:
                print("setor invalido")
            else:
                break

        registrador.funcionarios[setor] = funcionario
        return (f'funcionario {funcionario} registrado com sucesso no setor {setor}')

class ativo():
    def __init__(self,nome,setor):
        self.nome = nome
        self.setor = setor
        self.marca = None
        self.segmento = None

    

class mala ():
    def __init__(self, ferramental):
        self.responsavel = mala.verificar_responsavel()
        self.ferramental = mala.extrair_ferramentas() #elaborar lógica pois deve ser capaz: 1 - fazer uma mala de ferrametas do 0. 
                                                      #2 - extrair dados de um Db externo de mala. 3 - dar um modelo pronto ao usuário para poder alterar
    def verificar_responsavel(self):       
        print(registrador.funcionarios)
        funcionario = input((f"qual responsavel deseja desginar? "))

        if funcionario not in registrador.funcionarios.lower():
            return ("funcionario invalido")
        else:
            return funcionario
        #montar lógica de case para retornar funcionarios

    def extrair_ferramentas(self):
        #montar lógica apra extrair lista de mala de ferramentas
        #montar lógica de registro individual de ferramentas pela própria lógica a partir da classe ativos
        pass

    @classmethod
    def criar_mala(cls):
        self.responsavel
    