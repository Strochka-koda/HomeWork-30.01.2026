def even_fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        if a % 2 == 0:
            yield a
        a, b = b, a + b

for num in even_fibonacci(100):
    print(num, end=" ")