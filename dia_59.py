lista_tuplada = [("Quimica", 88 ), ("Lenguaje", 97), ("Fisica", 90)]
lista_ordenada = sorted(lista_tuplada, key=lambda _: _[1], reverse=False)
print(lista_ordenada)