print('Введите количество чисел (1 ≤ N ≤ 100000)')
n = int(input('N = '))

if n > 100_000:
    print('Превышен диапазон числел N')
else:
    numbers = set()
    numbersString = input('Введите числа через пробел: ')
    for number in list(map(int, numbersString.split(' '))):
        if number > 1_000_000_000:
            print(f'Число {number} больше 1_000_000_000')
        else:
            numbers.add(number)
    print(f'Количество уникальных значение = {len(numbers)}')
