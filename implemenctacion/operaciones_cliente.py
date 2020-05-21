import sys
sys.path.append('gen-py')

from servicio import Operaciones

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


if __name__ == '__main__':
    # Make socket
    transport = TSocket.TSocket('localhost', 9090)
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TBufferedTransport(transport)
    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # Create a client to use the protocol encoder
    client = Operaciones.Client(protocol)
    # Connect!
    transport.open()    
    try:                        
        def pedirOpcion():
            isCorrecto = False
            numeroEntero = 0
            while(not isCorrecto):
                try:
                    numeroEntero = int(input("Introduce un numero entero: "))
                    isCorrecto = True
                except ValueError:
                    print('Error, introduce un numero entero')    
            return numeroEntero

        salir = False
        opcion = 0
        while not salir:    
            print ("Bienvenido a la calculadora apache thrift.")    
            print ("1.- Sumar")
            print ("2.- Restar")
            print ("3.- Multiplicar")
            print ("4.- Dividir")
            print ("5.- Salir")

            print ("Elige una opcion")
            opcion = pedirOpcion()                        
            
            if opcion == 1:                
                numeroUno = float(input("Ingrese el primer numero: "))
                numeroDos = float(input("Ingrese el segundo numero: "))
                resultado = client.sumar(numeroUno, numeroDos)
                print(f"El resultado es: {resultado}")
            elif opcion == 2:                
                numeroUno = float(input("Ingrese el primer numero: "))
                numeroDos = float(input("Ingrese el segundo numero: "))
                resultado1 = client.restar(numeroUno, numeroDos)
                print(f"El resultado es: {resultado1}")
            elif opcion == 3:                                
                numeroUno = float(input("Ingrese el primer numero: "))
                numeroDos = float(input("Ingrese el segundo numero: "))
                resultado2 = client.multiplicar(numeroUno, numeroDos)
                print(f"El resultado es: {resultado2}")
            elif opcion == 4:                                
                numeroUno = float(input("Ingrese el primer numero: "))
                numeroDos = float(input("Ingrese el segundo numero: "))
                resultado3 = client.dividir(numeroUno, numeroDos)
                print(f"El resultado es: {resultado3}")
            elif opcion == 5:
                salir = True
            else:
                print ("Introduce un numero entre 1 y 5")    
        print ("Hasta luego")
    except InvalidOperation as e:
        print('InvalidOperation: %r' % e)
    # Close!
    transport.close()
            