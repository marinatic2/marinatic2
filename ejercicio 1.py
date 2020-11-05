'''
1. Escriba una función llamada “multiplicación” que reciba como argumento cuatro números reales
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
            
