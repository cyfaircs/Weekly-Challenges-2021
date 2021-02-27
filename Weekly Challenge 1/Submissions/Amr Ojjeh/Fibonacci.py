def fib(n):
    final = 0
    for i in fib_seq(n):
        final = i
    return final

def fib_seq(n):
    if n <= 1:
        yield n
    else:
        current = 1
        prev = 0
        yield current
        for i in range(n - 1):
            temp = current
            current = current + prev
            prev = temp
            yield current

print(f"fib(0) = {fib(0)}")
print(f"fib(1) = {fib(1)}")
print(f"fib(6) = {fib(6)}")

# Fibonacci Continued

n = int(input("Enter n: "))
s = 0
print("0", end="")
for i in fib_seq(n):
    if i % 2 != 0:
        print(f" + {i}", end="")
        s += i
print(f" = {s}")
