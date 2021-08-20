from typing import MutableSequence


def main():
    #escribe tu código abajo de esta línea
    pass
saldo= float(input("Dame el saldo del mes anterior:"))
ingresos= float(input("Dame los ingresos:"))
egresos= float(input("Dame los egresos:"))
cheques = int(input("Dame el número de cheques:"))
saldofinal = (((saldo+ingresos-egresos)+ (13*cheques))*0.75)
print (saldofinal)



if __name__ == '__main__':
    main()
