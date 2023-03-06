# hello world
print("hello world, jack")

# variable
msg = "hello python world"
print(msg)

msg = "variable is allowed to be changed"
print(msg)


first_name = "zhangtian"
last_name = "tian"
full_name = f"{first_name} {last_name}"
print(f"hello, {full_name.title()}")

print("python")
print("\tpython")
print("C\nJava\nC++")

str_with_space = " hhh shit "
print(str_with_space.rstrip())
print(str_with_space.lstrip())
print(str_with_space.strip())

print(2 + 3)
print(2 - 1)
print(3 / 2)

print(3 * 2)
print(3 ** 2)

print(0.2 + 0.3)

# multi variable 
x, y, z = 0, 1, 2
# consts
MAC_ADDR = "fd:ad:23:44"

bicycle = ['trek', 'giant', 'melida']

# index is started with 0
print(bicycle)
print(bicycle[1].title())

# add ele into array
# 1. append
a = ['t', 'z','a']
a.append('d')

print(a)
# 2. insert
a.insert(0, 'ttt')
print(a)

# 3. delete ele
# use del
del a[0] # delete 'ttt'
print(a)
# use pop
# default pop is last ele
v = a.pop()
print(v)
print(a)

# pop any idx
v2 = a.pop(1)
print(v2)
print(a)

# use remove(value) to delete first ele
# just remove the first ele match value, 
# make sure to use loop to delete all duplicated value
ele_to_remove = 'a'
a.remove(ele_to_remove)
print(a) # should be ['t']

# 3.3