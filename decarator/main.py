
def warning_func(func):
    def inner(*args, **kwargs):
        return 'Warning'
    return inner

@warning_func
def value(a,b,c):
    return 0


print(value(1, 2, 3))