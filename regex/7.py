import re
with open(r"row.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
a = ''.join(content)
tx = re.sub('_', ' ', a)
tx = tx.title()
tx = re.sub(' ', '', tx)
print(tx)