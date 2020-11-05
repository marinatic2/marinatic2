'''
Dime un número al azar entre 1 y 10 y lo adivino
'''
import random

def adivino_2():
    maxn=10
    numero=random.randint(1,maxn)
    intento=input("intentalo: ")
    while intento!=numero:
        if intento>numero:
            print "Demasiado grande"
        if intento<numero:
            print "Demasiado pequeño"
        intento=input("intentalo: ")
    print "Ahora has acertado"

adivino_2()
