"""def fun(n):
    #Base Case
    if n==0:
        return
    # recursive case
    print(n,end=" ")
    fun(n-1)

fun(5)

# Output: 5 4 3 2 1 """

def fun(n):
    #Base Case
    if n==0:
        return
    # recursive case
    fun(n-1)
    print(n,end=" ")
    

fun(5)
# Output: 1 2 3 4 5

# This is happend because of the stack. When we call a function, it is added to the stack. When the function returns, it is removed from the stack. In the
# first case, we are printing the value of n before calling the function, so the value of n is printed before the function is called. 
# In the second case, we are calling the function before printing the value of n, so the value of n is printed after the function is called.

