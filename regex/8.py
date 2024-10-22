import re
with open(r"row.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
a = ''.join(content)
tx = re.findall(r"[A-Z][a-z]*", a)
print(tx)