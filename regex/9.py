import re
with open(r"row.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
a = ''.join(content)
tx = re.sub(r"(\w)([A-Z])", r"\1 \2 ", a)
print(tx)