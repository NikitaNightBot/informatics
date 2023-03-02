import itertools
from textwrap import wrap
import random

with open('dict.txt', 'r', encoding='utf-8') as f:
    data = set([line.rstrip() for line in f.readlines()])

name_letters = input("Name: ")
surname_letters = input("Surname: ")

total = name_letters + surname_letters

buffer = {''}

count = int(input("Entropy: "))

wcount = int(input("Count of words to use in program: "))

letter_shufles = [''.join(random.sample(total, 7)) for _ in range(count)]


for shuffle in letter_shufles:
    words = itertools.permutations(shuffle)
    for word in words:
        if ''.join(word) in data:
            buffer.add(''.join(word))

buffer = [i for i in buffer if i]
delim = '\n    '
pascal_code = []
for word in random.sample(buffer, (wcount if wcount<=len(buffer) else len(buffer))):
    code = []
    for letter in word:
        try:
            state = "Name"
            idx = name_letters.index(letter)
        except:
            state = "Surname"
            idx = surname_letters.index(letter)
        code.append(f"{state}[{idx+1}]")
        
    pascal_code.append(f"writeln({'+'.join(code)});")

# print(pascal_code)

program = \
f"""
Program Homework;

Var Name, Surname: String;

begin
    Name:='{''.join(name_letters)}';
    Surname:='{''.join(surname_letters)}';
    {delim.join(pascal_code)}
end.

"""

print(program)