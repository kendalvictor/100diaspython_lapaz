import random

lista_random = []
for numero in range(5):
    lista_random.append(int(random.random()*numero*10+1))
    
print(sum(lista_random))
#uso "for"  directo porque entiendo obtuve puntaje 1 en el reto 48 por sar listas por compresion 