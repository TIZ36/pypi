from funcs import test_func2 as tt



# file
with open('f.txt') as file_obj:
    contents = file_obj.read()

print(contents)

with open('f.txt') as file_obj:
    for line in file_obj:
        print(line)

with open('f.txt', 'w') as file_obj:
    file_obj.write("i love python")
    
with open('f.txt', 'a') as file_obj2:
    file_obj2.write("i love python too")

# exception
try:
    print(5/0)
except ZeroDivisionError:
    print("can not use zero as divider")

filename = 'f.txt'

try:
    with open(filename, encoding='utf-8') as f:
        cc = f.read()
except FileNotFoundError:
    print("file not found")
else:
    word = cc.split()
    print(word)