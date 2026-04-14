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
