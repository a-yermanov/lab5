import re
with open(r"row.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
a = ''.join(content)
tx = re.sub('(.)([A-Z][a-z]+)', r'\1_\2 ', a)
tx = tx.lower()
tx = re.sub('([a-z0-9])([A-Z])', r'\1_\2', tx)
print(tx)