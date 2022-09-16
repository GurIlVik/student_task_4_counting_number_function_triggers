import datetime

# функция вычитания
def minus(a, b):
    save_open_function('minus')
    return a - b

# функция сложения
def plus(a, b):
    save_open_function('plus')
    return a + b

# функция записи данных
def save_open_function(name):
    lines = f'функция {name} открывалась {datetime.datetime.now()}. \n'
    with open('open_function.txt', 'a', encoding='utf-8') as fil:
        fil.write(lines)

# основная функция
def modify_func(func_in):
    def func_out(a, b):
        x = func_in(a, b)
        print('В результате должно получиться : ', x)
        print(f"Данные получены в {datetime.datetime.now()}")
        save_open_function('func_out')
        return x
    save_open_function('modify_func')
    return func_out

# функция открытия и чтения файла и распечатки
def open_file(num):
    count = 0
    list_chek = []
    with open('open_function.txt', 'r', encoding='utf-8') as file_check:
        for line in file_check:
            if num in line:
                count += 1
                list_chek.append(line)
    print(f'запрашиваемая Вами  функция {num} этой программы открвывались {count} раз, список открытий приведен ниже: \n')
    for x in list_chek:
        print(x[:-3])
    return True

# функция распорядитель
def distribute(num):
    if num == 'Not':
        return False
    return open_file(num)

# функция уточнения ввода пользователя по количеству использования функций
def check_work_function():
    password_cycle = True
    while password_cycle:
        answer_user = input(f'''
    Введите 1 если хотите получить полный отчет об открытии функция.
    введите 2 если интересует функция minus
    введите 3 если интересует функция plus
    введите 4 если интересует функция func_out
    введите 5 если интересует функция modify_func:
    введите 6 если хотите покинуть модуль
    ''')
        if answer_user < '1' or answer_user > '6':
            pass
        else: 
            if answer_user == '1':
                answer_user = 'функция'
            elif answer_user == '2':
                answer_user = 'minus'
            elif answer_user == '3':
                answer_user = 'plus'
            elif answer_user == '4':
                answer_user = 'func_out'
            elif answer_user == '5':
                answer_user = 'modify_func' 
            elif answer_user == '6':
                answer_user = 'Not'  
            password_cycle = distribute(answer_user)
    return True        

# функция ввода пользователя
def user_data():
    password_cycle = False
    while password_cycle == False:
        c = input('Для окончания программы введите стоп для продолжения всё что угодно: ').lower()
        print(c)
        if c == 'стоп':
            password_cycle = True
        else:
            a = input('Введите первое число: ')
            b = input('Введите второе число: ')
            if a < '0' or a > '9' and b < '0' or b > '9':
                continue
            else:
                a = int(a)
                b = int(b)
                new_plus = modify_func(plus)
                print(a, '+', b, '=', new_plus(a, b))
                new_minus = modify_func(minus)
                print(a, '-', b, '=', new_minus(a, b))
    return password_cycle

# функция проверки и создания файла при его отсутствии
def check_file():
    try:
        file1 = open('open_function.txt', 'r', encoding='utf-8')
    except IOError:
        file1 = open('open_function.txt', 'w', encoding='utf-8')
    file1.close()
    print(f'открыт файл - open_function.txt')

# модуль перезупуска программы
def start_program():
    check_file()
    password = True
    while password:
        answer_user = input(f"""
        Программа подсчета использования финкций на база функции сложения и вычитания: 
        Введите 1 - если хотите проверить сумму и разность
        Введите 2 - если необходимо посмотреть количество раз использования функций
        Введите 3 - если необходимо завершить программу
        """)
        if answer_user == '1':
            password = user_data()
        if answer_user == '2':
            password = check_work_function()
        if answer_user == '3':
            print('конец программе')
            password = False
            
            
if __name__ == "__main__":
    start_program()

