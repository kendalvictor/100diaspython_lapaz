import re

lista = ['+54 11 1234 5678', '+591 68754321', '+56 9 8765 4321']
validas = [re.sub(r'\+[0-9]+[ ]+', '', _) for _ in lista]
print(validas)