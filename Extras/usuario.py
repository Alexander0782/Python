#Alexander uribe 29/05
from Extras import tarjeta
from tarjeta import TarjetaCredito  

class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0
    def agregar_tarjeta(self, tarjeta):
        """Agrega una nueva tarjeta al usuario"""
        self.tarjetas.append(tarjeta)
        print(f"Tarjeta añadida para el usuario {self.nombre} {self.apellido}. Ahora tiene {len(self.tarjetas)} tarjeta(s).")
    def hacer_compra(self, monto, indice_tarjeta=0):
        """Realiza una compra en la tarjeta especificara (por indice)"""
        if 0<= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].comprar(monto)
        else:
            print(f"No existe la tarjeta con el indice {indice_tarjeta}.")
            return self
    def pagar_tarjeta(self, monto, indice_tarjeta=0):
        """Realiza un pago en la tarjeta especificada (por indice)"""
        if 0 <= indice_tarjeta < len(self.tarjetas):
            self.tarjetas[indice_tarjeta].pago(monto)
        else:
            print(f"No existe la tarjeta con el indice {indice_tarjeta}.")
            return self
    def mostrar_sald_usuario(self):
        """Muestra el saldo total a pagar del usuario"""
        print(f"Saldo de las tarjetas del usuario {self.nombre} {self.apellido}:")
        for i in enumerate(self.tarjeta,1):
            print(f"Tarjeta {i}: Saldo a pagar: ${tarjeta.saldo_pagar:,}")
        return self

#ejemplo de uso

