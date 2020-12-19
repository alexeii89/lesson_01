natural_number = int(input("Введите целое число: "))

i = 1
max = natural_number % 10
while natural_number == 0:
    if max < natural_number % 10:
        max = natural_namber % 10
        natural_number = natural_number // 10
    else:
        natural_number = natural_number // 10

    print(f"Большее число: {max}")
