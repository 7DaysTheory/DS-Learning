
eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
def de_cipher(lang: str, task: str, step: int, phrase: str) -> str:
    out=''
    if task == 'дешифр':
        if lang=='ru':
            for i in range(len(phrase)):
                if phrase[i].islower():
                    dig=rus_lower_alphabet[rus_lower_alphabet.find(phrase[i])-step]
                elif phrase[i].isupper():
                    dig=rus_upper_alphabet[rus_upper_alphabet.find(phrase[i])-step]
                else:
                    dig=phrase[i]
                out+=dig
        elif lang=='en':
            for i in range(len(phrase)):
                if phrase[i].islower():
                    dig=eng_lower_alphabet[eng_lower_alphabet.find(phrase[i])-step]
                elif phrase[i].isupper():
                    dig=eng_upper_alphabet[eng_upper_alphabet.find(phrase[i])-step]
                else:
                    dig=phrase[i]
                out+=dig
    elif task == 'шифр':
        if lang=='ru':
            for i in range(len(phrase)):
                if phrase[i].islower():
                    dig=rus_lower_alphabet[(rus_lower_alphabet.find(phrase[i])+step) % 32]
                elif phrase[i].isupper():
                    dig=rus_upper_alphabet[(rus_upper_alphabet.find(phrase[i])+step) % 32]
                else:
                    dig=phrase[i]
                out+=dig
        if lang=='en':
            for i in range(len(phrase)):
                if phrase[i].islower():
                    dig=eng_lower_alphabet[(eng_lower_alphabet.find(phrase[i])+step) % 26]
                elif phrase[i].isupper():
                    dig=eng_upper_alphabet[(eng_upper_alphabet.find(phrase[i])+step) % 26]
                else:
                    dig=phrase[i]
                out+=dig
    return out
def main():
    print('Добро пожаловать')
    lang = input('Укажите язык алфавита: ')
    task = input('Укажите задачу - шифрование или дешифрование? (шифр/дешифр) ')
    known = input('Известен ли шаг сдвига? ')
    if known.upper() == 'Y':
        step = int(input('Укажите шаг сдвига: '))
    phrase = input('Введите фразу: ')
    if known.upper() == 'Y':
        print(de_cipher(lang, task, step, phrase))
    else:
        if lang=='en':
            for i in range(25):
                print(de_cipher(lang, task, i, phrase))
        if lang=='ru':
            for i in range(32):
                print(de_cipher(lang, task, i, phrase))
main()