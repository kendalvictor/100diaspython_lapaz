from itertools import  chain


tupla_int = (78, 100) 
tupla_str = ("Dias", "Python")

resultado = list(map(type,  chain(tupla_int, tupla_str)))  
print(resultado)  
