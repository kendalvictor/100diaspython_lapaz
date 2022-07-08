from itertools import  filterfalse


lista =[1, 5, 10, 23, 3, 555, 11, 10]
resultado = list(filterfalse(lambda _: _ % 5, lista))
print(resultado)  

