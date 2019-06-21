class Conta:
    def __init__(self,numero, titular, saldo, limite):
        print("Construindo objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel

    def saca(self, valor):
        if (self.__pode_sacar(valor)):
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @property
    def titular(self):
        return self.__titular