# agrupam dados e métodos e manipulam esses dados em uma unidade
# Impõe restrições ao acesso direto a variáveis e métodos e pode evitar a modificação acidental de dados
# a variável de um objeto só pode ser alterada pelo método desse objeto
# público: só pode ser acessado fora da classe
# privado: só pode ser acessado pela classe

class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    def mostrar_saldo(self): # forma correta de usar um método privado
        return self._saldo


conta = Conta("001",100)
conta.depositar(100)
print(conta._saldo)
print(conta.nro_agencia)
print(conta.mostrar_saldo())