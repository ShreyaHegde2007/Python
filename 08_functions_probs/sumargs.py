def sum_of_args(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum_of_args(1,2,3,4,5,6,7))
