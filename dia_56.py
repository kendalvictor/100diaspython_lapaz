listado = [49, 4, 36, 16, 25]

lambda_raiz = lambda _: _**(1/2)

nueva_lista = [lambda_raiz(_) for _ in listado]
print(nueva_lista)