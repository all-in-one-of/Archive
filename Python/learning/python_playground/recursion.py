
def factorial(n):
    space = ' ' * (4 * n)
    print space, 'factorial', n
    if n == 0:
        print space, 'returning 1'
        return 1
    else:
        #n * factorial(n-1)
        result = n * factorial(n-1)
        print space, 'returning', result
        return result

def fibonacci(n):
    known = {0:0, 1:1}
    space = ' ' * (4 * n)
    print space, 'fibonacci', n
    if n in known:
        print space, 'returning', known[n]
        return known[n]
    else:
        f = (fibonacci(n-1) + fibonacci(n-2))
        known[n] = f
        print space, 'returning', f
        return f

print fibonacci(10)