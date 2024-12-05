def largerThanN(lst, n):
    result = [num for num in lst if num > n]
    return result


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 5
print("Numbers larger than", n, ":", largerThanN(lst, n))
