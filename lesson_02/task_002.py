s = input("введите значение списка через пробел: ")
my_list = s.split(" ")
i = 0
while i + 1 < len(my_list):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i = i + 2
print(my_list)
