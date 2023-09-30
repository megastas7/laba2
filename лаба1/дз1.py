a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print("Сумма числе: ", a + b)
print("Разность числе: ", a - b)
print("Произведение числе: ", a * b)
print("Среднее арифметическое этих чисел: ", (a + b) / 2)
#print(max(abs(a), abs(b)) - min(abs(a), abs(b)))
if a < 0:
    a = a * (-1)
if b < 0:
    b = b * (-1)
if a > b:
    maximum = a
    minimum = b
else:
    minimum = a
    maximum = b
print("Разность максимального и минимального по модулю: ", maximum - minimum)