import re


cadena = "Llevas programando 70 dias seguidos"

search = re.findall(r'[ ]*(\w+a\w+)[ ]*', cadena)
print(search)

