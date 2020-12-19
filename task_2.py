time_second = int(input("Введите время в секундах: "))
second = time_second % 60
minutes = (time_second // 60) % 60
hour = time_second // 3600

print(f"{hour}:{minutes}:{second}")
