my_list = []
i = 1
while True:
    my_command = input("Для добавление введите 'add', для анализа введите 'assay', для выхода введите 'q': ")
    if my_command == "add":
        name = input("Введите название товара: ")
        price = float(input("Введите цену товара: "))
        amount = int(input("Введите колличество товара: "))
        d = dict(название=name, цена=price, количество=amount, eд="шт.")
        my_tuple = (i, d)
        i = i + 1
        my_list.append(my_tuple)
        print(my_list)
    elif my_command == "assay":
        j = 0
        assay_dict = {}
        for key in my_list[j][1]:
            my_names = []
            for j in range(len(my_list)):
                my_names.append(my_list[j][1][key])
            dict2 = {key: my_names}
            print(key, my_names)
            assay_dict.update(dict2)
            j = j + 1
        print(assay_dict)
    elif my_command == "q":
        break
