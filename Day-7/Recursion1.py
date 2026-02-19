def fact(n):
    #Base Case
    if n==0:
        return 1
    # recursive case
    return n*fact(n-1)
print(fact(5))