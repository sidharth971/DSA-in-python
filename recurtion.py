'''
@Sidharth Sahoo
Recursion is a process in which a function call itself again and again
to solve a problem.
'''

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def printN(n):
    if n == 1:
        return 1
    printN(n-1)
    print(n, end=' ')
    return
def printNreverse(n):
    if n == 1:
        return 1
    print(n, end=' ')
    printN(n-1)
    return

if __name__ == "__main__":
    print(factorial(10))
    printN(10)
    print()
    printNreverse(10)