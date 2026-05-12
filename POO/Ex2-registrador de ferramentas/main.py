class registrador():

    ferramentas = {} #ferramentas é um dicionario de objetos sendo pesquisado a partir do atributo ferramentas.setor
    funcionarios = {} #funcionario é um dicionarios de objetos sendo pesquisado a partir do atributo funcionario.setor
    setores = [] #setor é um indíce para buscar ferramentas e funcionarios

    def cria_setor(self):
        setor = input("qual setor deseja registrar? ").upper()
        registrador.setores.append(setor)  
        return (f"setor {setor} registrado")                                

 
        
    def criar_funcionario(cls):# este método deve estar na calsse de funcionarios
        funcionario = input("qual funcionario deseja cadastrar? ").upper()
        print(registrador.setores)
        setor = input("para qual setor deseja designar? ").upper()

        if setor not in registrador.setores:
            print("setor invalido")
            return False

        registrador.funcionarios[setor] = funcionario
        return (f'funcionario {funcionario} registrado com sucesso no setor {setor}')
        return True

class ativo():#ativos serão pesquisados a partir do registro geral
    def __init__(self,nome,setor):
        self.nome = nome
        self.setor = setor
        self.marca = None
        self.segmento = None

    @classmethod# é necessário fazer classmethod para não ser dependente de um objeto que pode não existir
    def cria_ferramenta(cls):
        ferramenta = input("qual ferramenta deseja cadastrar? ").lower()
        print(registrador.setores)
        setor = input("para qual setor deseja designar? ").upper()

        if setor not in registrador.setores:
            print("setor invalido")
            return False

        registrador.ferramentas[setor] = ferramenta
        print(f'a ferramenta {ferramenta} registrada com sucesso no setor {setor}')
        return cls(ferramenta, setor)

class mala (): #mala deve ser uma classe dentro da classe funcionarios
    def __init__(self, ferramental):

        self.responsavel = mala.verificar_responsavel()

        self.ferramentas = [ "Chave de fenda","Chave Phillips","Chave inglesa","Chave Allen","Alicate universal","Alicate de corte","Alicate de bico",
        "Martelo","Trena","Nível","Furadeira","Parafusadeira","Brocas","Parafusos","Porcas","Arruelas","Estilete","Fita isolante","Multímetro","Lanterna","Abraçadeiras",
        "Serrote","Lixa","Luvas de proteção","Óculos de proteção" ]


    @classmethod # é necessário fazer classmethod para não ser dependente de um objeto que pode não existir
    def verificar_responsavel(cls):  
     
        print(registrador.funcionarios)
        funcionario = input(("qual responsavel deseja designar?")).upper()
        
        if funcionario in registrador.funcionarios:
            return funcionario
        else:
            print("funcionario invalido")

    
teste = registrador()

teste.cria_setor()

f = ativo(ativo.cria_ferramenta())

print(f.nome, f.setor)