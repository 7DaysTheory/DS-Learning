num_base_over_10 = [_ for _ in range(10, 36)]
ind_base_over_10 = [chr(i) for i in range(97, 123)]

def welcome():
    print('Добро пожаловать! Эта программа переводит числа из одной системы счисления в другую.')

def get_a_number() -> str:
    print('Введите число, которое хотите перевести в другую систему счисления.')
    return input('Введите число: ')

def is_valid_base(base: int) -> bool:
    return 2 <= base <= 36 

def get_base() -> int:
    while True:
        print('Введите основание системы счисления (от 2 до 36).')
        base = int(input('Введите основание: '))
        if is_valid_base(base):
            return base
        else:
            print('Основание системы счисления должно быть от 2 до 36. Попробуйте снова.')

def is_valid_number(number: str, base: int) -> bool:
    number=number.lower()
    for i in range(len(number)):
        if number[i].isdigit():
            if int(number[i])>=base:
                return False
        elif number[i].isalpha():
            if num_base_over_10[ind_base_over_10.index(number[i])]>=base:
                return False
        else:
            return False
        pass
    else:
        return True

def convert_num_to_decimal(number: str, base: int) -> int:
        out=0
        num=number[::-1].lower()
        for i in range(len(num)):
            if num[i].isalpha():
                out+=(num_base_over_10[ind_base_over_10.index(num[i])]*(base**i))
            else:
                out+=int(num[i])*(base**i)
            pass
        return out

def convert_num_from_decimal(number: str, base: int) -> str:
        out=''
        num=int(number)
        ls=[]
        while num//base>0:
            if num%base<10:
                ls.append(num%base)
            else:
                ls.append(ind_base_over_10[num_base_over_10.index(num%base)].upper())
            num//=base
        ls.append(num)
        ls=ls[::-1]
        for i in range(len(ls)):
            out+=str(ls[i])
        return out

def main_decimal():
    """Данная функция финализирует перевод числа из любой системы исчисления(до 36) в десятичную
    """
    while True: 
        num=str(get_a_number())
        base=get_base()
        if not is_valid_number(num, base):
                print(f'Введите число с основанием {base}')
        else:
            print(f'Число {num} в десятичной системе счисления равно {convert_num_to_decimal(num, base)}')
            break

def main_base():
    while True: 
        num=str(get_a_number())
        base=10
        to_base=int(input('Введите основание для конвертации: '))
        if not is_valid_number(num, base):
                print('Введите число с основанием 10')
        else:
            print(f'Число {num} в {to_base}-ой системе счисления равно {convert_num_from_decimal(num, to_base)}')
            break

def task():
    task=input('Что делаем? Переводим число в десятичную или наоборот? (dec/base):  ')
    while True:
        if task=='dec':
            main_decimal()
        elif task=='base':
            main_base()
        else:
            print('Введите корректный вариант')

def main():
    welcome()
    task()


main()