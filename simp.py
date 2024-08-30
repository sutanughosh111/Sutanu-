def fibonacci(n):
    fib_sequence = [0, 1]  # Starting the series with 0 and 1
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
n = 10  # Length of the Fibonacci series
print(fibonacci(n))
