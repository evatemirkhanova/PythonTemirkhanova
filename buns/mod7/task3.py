# снова запишем декораторы validate_args и memoize

def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

# напишем декоратор timer, который будет замерять время выполнения функции:
import time

def timer(func):    
    def wrapper(*args, **kwargs):
        start_time = time.time()          # запоминаем текущее время
        result = func(*args, **kwargs)    # вызываем декорируемую функцию
        end_time = time.time()            # запоминаем время выполнения функции
        execution_time = end_time - start_time  # вычисляем время выполнения
        print(f"Время выполнения функции {func.__name__}: {execution_time:.20f} секунд")
        return result                    # возвращаем результат выполнения    
    return wrapper

# Затем, мы можем применить все три декоратора к функции fibonacci:
#@timer
#@memoize
@validate_args
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


fib_without_memoize = timer(fibonacci)
print('Фибоначчи без memoize с аргументом 35: ', fib_without_memoize(35))

fibonacci = memoize(fibonacci) 
fib_with_memoize = timer(fibonacci)     
print('Фибоначчи с memoize и аргументом 35: ', fib_with_memoize(35))  












# далее закоменчено старое продолжение кода, которое работает, но верхний уже полноценный код и верно выполняет все нужды :)

# Теперь мы можем сравнить скорость выполнения функции fibonacci с декоратором memoize и без него с помощью декоратора timer:
#print('Фибоначчи с аргументом 60: ', fib(60))       # вызовет функцию fibonacci с аргументом 30.
                           # Декоратор timer запишет время выполнения функции fibonacci и выведет его в консоль.

# Если мы хотим сравнить скорость выполнения функции fibonacci с декоратором memoize и без него,
# мы можем вызвать функцию дважды и сравнить время выполнения:
'''
start_time = time.time()
fibonacci(30)
end_time = time.time()
execution_time_without_memoize = end_time - start_time

start_time = time.time()
fibonacci(30)
end_time = time.time()
execution_time_with_memoize = end_time - start_time

print(f"Время выполнения функции fibonacci без декоратора memoize: {execution_time_without_memoize} секунд")
print(f"Время выполнения функции fibonacci c декоратором memoize: {execution_time_with_memoize} секунд")

"""
 Таким образом, мы можем сравнить время выполнения функции fibonacci
 с декоратором memoize и без него, используя декоратор timer:
 
Время выполнения функции fibonacci без декоратора memoize: 0.0 секунд
Время выполнения функции fibonacci c декоратором memoize: 0.0 секунд
"""
'''