#  Biblioteca Musical — Exercício 1

Exercício de Programação Orientada a Objetos desenvolvido como parte de um plano de estudos estruturado para o mercado de desenvolvimento. O objetivo foi construir um sistema de cadastro de artistas e músicas aplicando conceitos de POO na prática.

---

## O que o sistema faz

- Cadastra artistas e suas músicas
- Detecta duplicatas de artistas e músicas
- Mantém uma discografia por artista
- Reutiliza objetos existentes em vez de criar instâncias desnecessárias
- Gerencia IDs únicos por artista

---

## Decisões de Design

### Inputs fora da classe
A coleta de dados do usuário foi mantida intencionalmente fora da classe `Registro`. Essa decisão separa a responsabilidade de **coletar** dado da responsabilidade de **processar** dado — princípio que futuramente facilitará a substituição da interface de linha de comando por uma API ou front end sem necessidade de alterar a lógica central.

### Reutilização de objetos via lista de instâncias
Em vez de criar um novo objeto `Registro` sempre que um artista já cadastrado adiciona uma música, o sistema localiza o objeto existente na lista `Artistas` e o reutiliza. Isso evita duplicidade de estado e mantém a discografia centralizada na instância correta.

### Classe simplificada e sem `@classmethod`
Uma versão anterior utilizava `@classmethod` como ponto de entrada para criação de instâncias. Após revisão, optei por remover esse padrão pois a lógica de entrada foi movida para fora da classe, tornando o classmethod desnecessário neste contexto.

### Retorno semântico de `Registrar_artista`
O método retorna o objeto do artista caso ele já exista, ou `False` caso seja um cadastro novo. Essa convenção permite que o código externo tome decisões de fluxo sem precisar acessar internamente os atributos da classe.

---

## Trajetória do Exercício

### Versão 1
A primeira implementação concentrava toda a lógica em uma única classe — cadastro, busca, input e controle de fluxo. O `@classmethod` era o ponto central de entrada e os atributos de classe misturavam responsabilidades de coleção e de instância. O código funcionava mas apresentava bugs silenciosos como argumentos invertidos no construtor e contador de ID que nunca incrementava.

### Versão 2 (atual)
Refatoração com foco em três mudanças principais: separação dos inputs para fora da classe, reutilização de objetos existentes e simplificação da estrutura. A classe ficou mais coesa e o fluxo externo mais legível.

---

## O que ainda será refatorado

Este exercício será retomado futuramente como parte do estudo de banco de dados. As melhorias planejadas incluem:

- Separação em duas classes: `Artista` e `Catalogo`
- Eliminação de atributos de classe mutáveis (`Artistas = []`, `musicas = []`)
- Persistência dos dados em banco de dados relacional

---

## Conceitos Praticados

- Classes e instâncias
- Atributos de classe vs atributos de instância
- `__str__` para representação legível
- Busca em lista de objetos
- Controle de fluxo externo baseado em retorno de métodos
- Separação entre coleta e processamento de dados

---

