print('Введите количество чисел (1 ≤ N ≤ 100000)')
n = int(input('N = '))
if n > 100_000:
    print('Превышен диапазон числел N')
else:
    numbers = set()
    for i in range(n):
        number = int(input(f'Число #{i + 1} = '))
        if number > 1_000_000_000:
            print('Число больше 1_000_000_000')
        else:
            numbers.add(number)
        break

    print(f'Количество уникальных значение = {len(numbers)}')
