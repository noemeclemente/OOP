# modificar a implementação interna sem alterar a API pública da classe
# pra retornar um valor é necessário ter o property anotado
# pra que seja possível atribuir um valor, é necessário ter o setter
# pra deletar é necessário o deleter

class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("Noeme", 2004)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")