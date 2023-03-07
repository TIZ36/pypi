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
a.append('3')
a.append('4')
a.append('5')
a.sort()
print(a)

a.sort(reverse=True)
print(a)

# use sorted() LINSHI PAIXU
print(sorted(a))
print(a)

# use to x.reverse() to reverse list
a.reverse()
print(a)

print(len(a))

# use -1 , last ele in list
print(a[-1])

# for in
for ele in a:
    print(ele)

# for range
for value in range(1, 5):
    print(value)

# range to build list
nums = list(range(1, 6))
print(nums)    

# range with step
nums = list(range(1, 6, 2))
print(nums)

ss = []
for v in nums:
    ss.append(v ** 2)

print(ss)

print(min(ss))
print(max(ss))
print(sum(ss))

# list-build for
ll = [value ** 3 for value in range(1, 11)]
print(ll)

# slice
# [start, end)
print(ss[0:2])

# all ele
print(ss[:4])
print(ss[0:])
print(ss[:])


# all ele without last one
print(ss[:-1])

# last 2 ele
print(ss[-2:])

# refer
s2 = ss
# copy
s3 = ss[:]

s2.append('r')
s3.append('z')

print(ss)
print(s2)
print(s3)

# tuple
tuple = (0, 1, 2)
print(tuple[0])
print(tuple[1])
print(tuple[2])

tupel = (2, 3, 4)
print(tupel)

# if
# if else
for ele in ll:
    if ele < 100 and ele > 3 or ele > 11 or ele in ll:
        print(ele)
    else:
        print('xx')

# if elif else

a = 'za'
if a == 'z' :
    print(a)
elif a == 'za':
    print(a, "dd")
else:
    print(a)

# dic
dic0 = {'a': 3, 'b': 4}

dic0 = {4: 3, 55: 4}
del dic0[55]
print(dic0)
print(dic0[4])

empty_dic = {'age': 44}
empty_dic['name']='zhangtian'
print(empty_dic)


age = empty_dic.get('age', 44)
print(age)

# traverse dic
for k, v in empty_dic.items():
    print('K:', k, 'V:', v)
for k in empty_dic.keys():
    print(k)
for v in empty_dic.values():
    print(v)