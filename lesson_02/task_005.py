my_list = [7, 5, 3, 3, 2]
while True:
    my_add = input("добавить значение в рейтинг (для выхода введите q): ")
    if my_add == "q":
        break
    elif my_add.isdigit() == True and 0 <= int(my_add) <= 9:
        my_list.append(int(my_add))
        my_list.sort(reverse=True)
        for i in range(len(my_list)):
            print(my_list[i], end=", ")
        print()
    else:
        print("Error. Try again")
