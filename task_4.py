natural_number = input("Введите целое число: ")

i = 1
max = int(natural_number[0])
while i < len(natural_number):
    if max < int(natural_number[i]):
        max = int(natural_number[i])
        i += 1
    else:
        i += 1

print(f"Большее число: {max}")

