my_list = [32, 47.93, "Привет", True, [2, "str"], (2, 7, 5.67), {'r': 'dict', 'h': 0.67}]
for i in range(len(my_list)):
    if type(my_list[i]) == list or type(my_list[i]) == tuple:
        print("\nВнутри типа ", type(my_list[i]), " типы: ")
        for j in range(len(my_list[i])):
            print(type(my_list[i][j]))

    elif type(my_list[i]) == dict:
        print("\nВнутри типа ", type(my_list[i]), " типы: ")
        for key in my_list[i]:
            print(type(my_list[i][key]))

    else:
        print(type(my_list[i]))
