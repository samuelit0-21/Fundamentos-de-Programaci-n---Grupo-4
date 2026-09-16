# Creamos una clase llamada CuentaBancaria.
# Esta clase representa una cuenta bancaria con titular y saldo.
class CuentaBancaria:

    # El constructor __init__ se ejecuta automáticamente
    # cuando creamos un objeto de esta clase.
    def __init__(self, titular, saldo):

        # Guardamos el nombre del titular.
        # Es un atributo público porque no tiene "__".
        self.titular = titular

        # Guardamos el saldo de la cuenta.
        # Los dos guiones bajos "__" indican que es un
        # atributo privado mediante Name Mangling.
        self.__saldo = saldo


    # Creamos un método para depositar dinero.
    # "monto" representa la cantidad que queremos agregar.
    def depositar(self, monto):

        # Comprobamos que el monto sea mayor que 0.
        # Esto evita depósitos negativos o iguales a cero.
        if monto > 0:

            # Sumamos el monto al saldo privado.
            self.__saldo += monto


    # Creamos un método para consultar el saldo.
    def ver_saldo(self):

        # Retornamos el valor del atributo privado.
        return self.__saldo


# Creamos un objeto llamado "c".
# El titular será "Ana" y el saldo inicial será 500.
c = CuentaBancaria("Ana", 500)

# Depositamos 200 en la cuenta.
# El saldo pasa de 500 a 700.
c.depositar(200)

# Consultamos el saldo mediante el método ver_saldo().
print(c.ver_saldo())  # 700
