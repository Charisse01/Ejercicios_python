# Recursividad de funciones en python por medio de la secuencia de Fibonacci

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

for x in range(1, 10):
    print(fibonacci(x))

#print("------------------------------------")

# Esta es otra forma 

# def fibonacci(n):
#   if n == 0 or n == 1:
#        return n
#    else:
#       return fibonacci(n - 2) + fibonacci(n - 1)

#for x in range(10):
#    print(x, fibonacci(x))
