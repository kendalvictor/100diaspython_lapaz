from itertools import  takewhile


lista = [2, 3, 5, 7, 13, 103, 25, 15, 45]
resultado = list(takewhile(lambda _: '0' not in str(_), lista))
print(resultado)  


