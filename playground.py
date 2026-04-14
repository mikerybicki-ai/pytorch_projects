# Create function that takes two arguments: one is list of elements (floats), seconde one is one integer argument. Second argument indicates number of elements, that has to be used to calculate moving average.



def mov_avg(x:list, z: int)-> float:

    sum = 0
    for i in range(z):
        sum += x[i]

    return (sum/z)



x = [2, 5, 1, 4, 6, 2, 0]

res = mov_avg(x, 4)
print(f"Moving avg is: {res}")