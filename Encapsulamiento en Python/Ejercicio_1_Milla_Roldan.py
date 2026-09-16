class CuentaBancaria:
def __init__(self, titular, saldo):
self.titular = titular # público
self.__saldo = saldo # privado
def depositar(self, monto):
if monto > 0:
self.__saldo += monto
def ver_saldo(self):
return self.__saldo
c = CuentaBancaria("Ana", 500)
c.depositar(200)
print(c.ver_saldo()) # 700
