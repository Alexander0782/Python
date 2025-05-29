#Alexander Uribe 29/05

class TarjetaCredito:
    tarjeta = []
    def __init__(self, saldo_pagar=0, limite_credito=100000, interes=0.02):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.interes = interes
        TarjetaCredito.tarjeta.append(self)
    def comprar(self, monto):
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto
            print(f"Compra realizada: ${monto:,}. Nuevo saldo: ${self.saldo_pagar:,}")
        else:
            print("Targeta rechazada, haz alcanzado el limite de credito")
        return self
    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        print(f"Pago realizado: ${monto:,}. Nuevo saldo: ${self.saldo_pagar:,}")
        return self
    def mostrar_info_tarjeta(self):
        print("<-------- Información de la tarjeta: --------->")
        print(f"Saldo a pagar: ${self.saldo_pagar:,}")
        print(f"Límite de crédito: ${self.limite_credito:,}")
        print("<----------------------------------------------->")
        return self
    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.interes
        print(f"Interés cobrado. Nuevo saldo: ${self.saldo_pagar:,.2f}")
        return self
    @classmethod
    def mostrar_todas_tarjetas(cls):
        for i, tarjeta in enumerate(cls.tarjeta, 1):
            print(f"Tarjeta {i}: saldo:${tarjeta.saldo_pagar:,} , Límite:${tarjeta.limite_credito:,}: Interés:{tarjeta.interes:.2%}")
            tarjeta.mostrar_info_tarjeta()

print("<-------- Tarjetab 1: --------->")
tarjeta1 = TarjetaCredito()
tarjeta1.comprar(50000).comprar(20000).pago(10000).cobrar_interes().mostrar_info_tarjeta()
print("<------------------------------>")
print("                                ")

print("<-------- Tarjeta 2: --------->")
tarjeta2 = TarjetaCredito(limite_credito=300000)
tarjeta2.comprar(70000).comprar(50000).pago(40000).cobrar_interes().mostrar_info_tarjeta()
print("<------------------------------>")
print("                                ")

print("<-------- Tarjeta 3: --------->")
tarjeta3 = TarjetaCredito(limite_credito=100000)
tarjeta3.comprar(30000).comprar(30000).cobrar_interes().mostrar_info_tarjeta()
print("<------------------------------>")



# tarjeta1 = TarjetaCredito(limite_credito=200000, interes=0.02)
# tarjeta1.comprar(50000)
# tarjeta1.pago(30000)
# tarjeta1.mostrar_info_tarjeta()
# tarjeta1.cobrar_interes()