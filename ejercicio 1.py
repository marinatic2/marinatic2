'''
1. Escriba una funci�n llamada �multiplicaci�n� que reciba como argumento cuatro n�meros reales
distintos de cero y que devuelva su producto.
'''
def multiplicacion():
    acumuladora=1
    print"Introduce un numero:"
    for cont in range (1,5):
        print "NUMERO", cont
        numero= input()
        acumuladora=acumuladora*numero
    print "PRODUCTO=", acumuladora
            
