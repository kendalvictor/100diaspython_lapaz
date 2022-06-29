import re

lista = ['192.08.001.5', '10.120.023.001', '192.60.2.1']
validas = [re.sub(r'\.[0]+', '.', _) for _ in lista]
print(validas)