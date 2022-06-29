import re

cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"

search = re.findall(r'a+b+', cadena)
print(search)