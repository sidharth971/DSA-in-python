'''
@Sidharth Sahoo
Recursion is a process in which a function call itself again and again
to solve a problem.
'''


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def printN(n):
    if n > 0:
        printN(n - 1)
        print(n, end=' ')


def printNreverse(n):
    if n > 0:
        print(n, end=' ')
        printNreverse(n - 1)


def printoddnumbers(n):
    if n > 0:
        printoddnumbers(n - 1)
        print(2 * n - 1, end=' ')


def printevennumbers(n):
    if n > 0:
        printevennumbers(n - 1)
        print(2 * n, end=' ')


def printevennumbersreverse(n):
    if n > 0:
        print(2 * n, end=' ')
        printevennumbersreverse(n - 1)


def printoddnumbersreverse(n):
    if n > 0:
        print(2 * n - 1, end=' ')
        printoddnumbersreverse(n - 1)


def sumofnaturalnumber(n):
    if n == 0:
        return 0
    return n + sumofnaturalnumber(n - 1)


def sumofnaturalnumberodd(n):
    if n == 0:
        return 0
    return 2 * n - 1 + sumofnaturalnumberodd(n - 1)


def sumofnaturalnumbereven(n):
    if n == 0:
        return 0
    return 2 * n + sumofnaturalnumbereven(n - 1)


def squere(n):
    if n == 0:
        return 0
    return n * n + squere(n - 1)


if __name__ == "__main__":
    print(factorial(10))
    printN(10)
    print()
    printNreverse(10)
    print()
    printoddnumbers(10)
    print()
    printevennumbers(10)
    print()
    printevennumbersreverse(10)
    print()
    printoddnumbersreverse(10)
    print()
    print(sumofnaturalnumber(10))
    print(sumofnaturalnumberodd(10))
    print(sumofnaturalnumbereven(10))
    print(squere(10))
