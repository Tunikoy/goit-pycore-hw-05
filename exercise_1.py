def caching_fibonacci():
    # порожній словник для кеш
    cache = {}

    # числа Фібоначчі
    def fibonacci(n):
        # Базові випадки: F(0) = 0, F(1) = 1
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Якщо значення в кеші, повертаємо його
        if n in cache:
            return cache[n]

        # екурсивно та зберігаємо у кеші
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію
    return fibonacci

# Приклад використання
fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610
