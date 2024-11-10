# Изначальный словарь с именами и адресами
people = {
    'Влад': 'Минск',
    'Илья': 'Витебск',
    'Даниил': 'Брест'
}

while True:
    print("\nВыберите действие:")
    print("1. Просмотреть словарь")
    print("2. Изменить адрес человека")
    print("3. Удалить человека")
    print("4. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        print("\nТекущий словарь:")
        for name, address in people.items():
            print(f"{name}: {address}")

    elif choice == '2':
        name = input("Введите имя человека, адрес которого хотите изменить: ")
        if name in people:
            new_address = input(f"Введите новый адрес для {name}: ")
            people[name] = new_address
            print(f"Адрес для {name} обновлен на: {new_address}")
        else:
            print(f"Человек с именем {name} не найден в словаре.")

    elif choice == '3':
        name = input("Введите имя человека, которого хотите удалить: ")
        if name in people:
            del people[name]
            print(f"{name} был удален из словаря.")
        else:
            print(f"Человек с именем {name} не найден в словаре.")

    elif choice == '4':
        print("Выход из программы.")
        break

    else:
        print("Неверный ввод. Пожалуйста, попробуйте снова.")