my_string = input("Введите несколько слов: ")
my_list = my_string.split(" ")
for i in range(len(my_list)):
    print(f"{i+1}\t{my_list[i][:10]}")