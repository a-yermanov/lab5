import re
with open(r"row.txt", 'r', encoding='utf-8') as file:
    content = file.readlines()
a = ''.join(content)
tx = re.compile("[a-z]*_[a-z]*")
m = tx.findall(a)
print(m)