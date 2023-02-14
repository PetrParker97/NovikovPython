#tasks 1

n = int(input('Введите число: '))

if n > 7:
    print('Привет' + '!')
else:
    print('Ошибка')

#tasks 2

name = str(input('Введите ваше имя: '))

if name == 'Вячеслав':
    print('Привет', name + '!')
else:
    print('Нет такого имени')

#tasks 3

array = [10, 20, 30, 50, 60, 70, 90,  265, 287, 347, 389, 500, 1000, 130, 160, 120]
n = []

for i in array:
    if i % 3 == 0:
        n.append(i)
print(n)


