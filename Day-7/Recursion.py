def printNNumbers(i,n):
    #Base Case
    if i>n:
        return 
    # recursive case
    print(i,end=" ")
    printNNumbers(i+1,n)

printNNumbers(1,10)
