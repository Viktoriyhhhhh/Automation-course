
def bank():
    x = int(input('Введите сумму вклада '))
    y = int(input('Введите желаемый срок вклада в годах '))
    for i in range(y):
        x += int(x * 0.1)
    return x
print(bank())
