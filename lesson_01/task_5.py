proceeds = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
earnings = proceeds - costs
if earnings < 0:
    print("Убыток составил:", (earnings * -1))
else:
    print("Прибыль составила:", earnings, "\nРентабельность:", ((earnings / costs) * 100), "%")
    personal = int(input("Введите численость сотрудников: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника составила: {(earnings / personal):.2f}")
