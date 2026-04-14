import itertools


x = 1
y = 1
z = 2
n = 3

l = [x, y, z]
print(l)

new_ob = itertools.permutations(l,)
print(f' yeah {list(new_ob)}')

#result = [x for x in new_ob if sum(x) != n]
#print(result)

# %%

x = [2, 3, 6, 6, 5]
x_sorted = sorted(set(x))
x_sorted[-2]

# %%
x = [2, 3, 6, 6, 5]
first = float('-inf')
second = float('-inf')

for el in x:
    if el > first:
        second = first
        first = el
        print(f"if {el}")
    elif first > el > second:
        second = el
        print(f'elif {el}')
print(second)
# %%
from collections import deque

a = [4]
d = deque(a)
l = d.popleft()
d

# %%
s = 'abbceed'
unique_letters = list(set(s))
dict_of_letters = dict(map(lambda x: (x, 0), unique_letters))
dict_of_letters['a'] += 1
for k, v in dict_of_letters.items():
    print(k, v)
print(type(dict_of_letters.items()))
new_dict = dict(map(lambda x: (x, 0), unique_letters))
new_dict
# %%
word = 'bafdce'
new_dict = dict(map(lambda x: (x, 0), set(word)))
new_dict.items()