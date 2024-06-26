def math(a, b):
    summa = a + b
    zero = a * b
    minus= a - b
    dev = 0
    try:
        dev = a / b
    except ZeroDivisionError:
        print('Вы делите на ноль!')
    return summa, zero, minus, dev

print(math(3, 3))
print(math(a=3,b=3))