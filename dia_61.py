import re
lista = ['20200806', 'jun122022', '202204DD', '20221208', '22mar2022']
numericas = list(filter(lambda _: re.search('\d+', _)[0] == _, lista))
print(numericas)

