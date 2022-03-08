def sum_reccursive(n):
    if n == 1:
        return 1
    else:
        r=(sum_reccursive(n-1) + n)
    return r

s = sum_reccursive(5)
print(s)