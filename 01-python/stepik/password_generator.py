import random as rm
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars=''
cnt_passwords = int(input('Укажите количество паролей: '))
len_passwords = int(input('Укажите длину одного пароля: '))
inc_dig = True if input('Нужно ли включить цифры? (y/n) ').lower() == 'y' else False
inc_low = True if input('Нужно ли включить прописные буквы? (y/n) ').lower() == 'y' else False
inc_up = True if input('Нужно ли включить заглавные буквы? (y/n) ').lower() == 'y' else False
inc_symb = True if input('Нужно ли включить символы? (y/n) ').lower() == 'y' else False
exc_vague = True if input('Нужно ли исключить неоднозначные символы? (il1Lo0O) (y/n) ').lower() == 'y' else False
if inc_dig:
    chars+=digits
if inc_low:
    chars+=lowercase_letters
if inc_up:
    chars+=uppercase_letters
if inc_symb:
    chars+=punctuation
if exc_vague:
    for c in chars:
        if c in 'il1Lo0O':
            chars=chars.replace(c,'')
def generate_password(lenght, chars):
    for i in range(cnt_passwords):
        print(''.join(rm.sample(chars, lenght)))
generate_password(len_passwords, chars)