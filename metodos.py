# métodos de classe: estão ligados à classe e não ao objeto
# tem acesso a estado da classe
# métodos estáticos: não recebe um primeiro argumento explicito, vinculado a classe e não ao objeto
# método de classe é usado para criar métodos de fábrica
# métodos estáticos para criar funções utilitárias

class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18



# p = Pessoa("André", 8)
# print(p.nome, p.idade)

p = Pessoa().criar_data_nascimento(1994, 3, 21, "Alice")
print(p.nome, p.idade)

print(Pessoa.maior_idade(18))
print(Pessoa.maior_idade(8))