from itertools import  starmap  


lista = [(2, 4, 6), (7, 8, 5, 6), (5, 10)]
maximos = list(starmap(max, lista))
print(maximos)