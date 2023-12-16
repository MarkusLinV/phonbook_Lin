# Задача №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество
# , номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# 1) Создание файла. +
# 2) Добавление новой записи +
    # 2*1)Забрать ввод пользователя
    # 2*2) открытие файла на дозапись
    # 2*3)Записать в фаил
# 3)Вывод на экран+
    # 3.1) Открыть фаил на чтение
    # 3.2) Считывание данных
    # 3.3) Вывод на экран
# 4) Поиск контакта
    # 4.1) Выбрать вариант поиска
    # 4.2) Забрать ввод пользователя
    # 4.3) Открытие файла на чтение
    # 4.4) Считать данные
    # 4.5) Осуществление поиска
    # 4.6) Вывести результат поиска
# 5) Создание интерфейса
def name_input():
    return input('Введите имя: ').title()


def surname_input():
    return input('Введите фамилию: ').title()


def patronymic_input():
    return input('Введите отчество: ').title()


def phone_input():
    return input('Введите номер: ')


def address_input():
    return input('Введите адрес: ').title()


def create_contact():
    '''Add an entry'''
    surname = surname_input()
    name = name_input()
    patronymic = patronymic_input()
    phone = phone_input()
    address = address_input()

    return f'{surname} {name} {patronymic} {phone}\n{address}\n\n'

def write_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding= 'utf-8') as file:
        file.write(contact)
        print('Контакт записан!')

def print_contact():
    '''List all entries'''
    with open('phonebook.txt', 'r+', encoding= 'utf-8') as file:
        print('---------------------')
        print(file.read())
        print('---------------------')


def seerch_contact(field = ''):
    ''''''

    print('Возможные варианты поиска:\n'
                '1. по фамилии\n'
                '2. по имени\n'
                '3. по отчеству\n'
                '4. по номеру\n'
                '5. по городу')
        
    index_var = int(input('Введите вариант:')) - 1

    search = input('Введите данные поиска:')
    with open('phonebook.txt', 'r+', encoding= 'utf-8') as file:
        contact_str = file.read()
    # print([contact_str])
    contacts_list = contact_str.strip().split('\n\n')
    # print(contacts_list)
    for contact_str in contacts_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[index_var]:
            print(f'\n{contact_str}\n')

def copy_contact():
    index_var = None
    contact_str = None
    contact_list = None
    with open('phonebook.txt', 'r+', encoding= 'utf-8') as file:
        print('---------------------')
        print(file.read())
        print('---------------------')
    index_var = int(input('Выберите контакт для копирования:')) - 1
    with open('phonebook.txt', 'r+', encoding= 'utf-8') as file:
        contact_str = file.read()
        # print([contact_str])
        contact_list = contact_str.split('\n\n')
        # print(contact_list)
        contact = contact_list[index_var]

        with open('copybook.txt' ,'a' ,encoding= 'utf-8') as file:
            file.write(f'{contact}\n\n')
            print('Контакт скопирован!')


def interface():
    with open('phonebook.txt' ,'a' ,encoding= 'utf-8'):
        pass
    
    user_input = None
    while user_input !=5:
        print('Выберите вариант действия:\n'
            '1. Добавить контакт\n'
            '2. Вывод списка контактов\n'
            '3. Поиск контактов\n'
            '4. Копировать в новый фаил\n'
            '5. Выход из программы')
        
        user_input = input('Введите вариант:')

        while user_input not in ('1', '2', '3', '4'):
            print('Некорректный ввод')
            user_input = input('Введите вариант:')

        print()

        match user_input:
            case '1':
                write_contact()
            case '2':
                print_contact()
            case '3':
                seerch_contact(field = '')
            case '4':
                copy_contact()
        print()
        
if __name__ == '__main__':
    interface()