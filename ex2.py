
# Exercício 2 - Verificação se número pertence à sequência de Fibonacci

def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    if n in fib:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."

# Teste com o número 21
numero = 21
print(fibonacci(numero))
