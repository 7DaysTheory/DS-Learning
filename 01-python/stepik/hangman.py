import random

word_list = ['печка', 'малыш', 'завод', 'олень', 'салют', 'пакет', 'дудка', 'мишка', 'экран', 'крыша', 'штаны', 'банка', 'шляпа', 'позор', 'кепка']

def get_word() -> str:
    """
    Выбирает случайное слово из списка для угадывания
    """
    return random.choice(word_list)

def display_hangman(tries: int) -> str:
    """Возвращает рисунок виселицы, подходящий к оставшемуся количеству попыток

    Args:
        tries (int): Кол-во оставшихся попыток. Пример: 0 - не осталось попыток

    Returns:
        str: Рисунок повешенного человечка
    """
    stages = [
    '''
    --------
    |      |
    |      0
    |     \\|/
    |      |
    |     / \\ 
    |
    ''',
    '''
    --------
    |      |
    |      0
    |     \\|/
    |      |
    |     / 
    |
    ''',
    '''
    --------
    |      |
    |      0
    |     \\|/
    |      |
    |    
    |
    ''',
    '''
    --------
    |      |
    |      0
    |     \\|
    |      |
    |    
    |
    ''',
    '''
    --------
    |      |
    |      0
    |      |
    |      |
    |     
    |
    ''',
    '''
    --------
    |      |
    |      0
    |     
    |      
    |     
    |
    ''',
    '''
    --------
    |      |
    |      
    |     
    |      
    |     
    |
    '''
    ]
    return stages[tries]

def welcome(cnt: int):
    if cnt==0:
        print('Добро пожаловать в "Виселицу"!')

def play(word: str):
    word_completition = '_'*len(word) #строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False #флаг 
    guessed_letters = [] #cписок уже названных букв
    guessed_words = [] #список уже названных слов
    tries = 6 #количество попыток
    print(display_hangman(tries))
    print(word_completition)
    while not guessed:
        guess = input('Введите слово: ').lower()
        if not guess.isalpha():
            print('Мне кажется это не слово...')
            continue
        elif guess in guessed_words:
            print('Вы уже вводили это слово, попробуйте другое')
            continue
        elif guess==word:
            print('Поздравляю, вы угадали!!!')
            return True
        elif tries == 0:
            print('Он умер...')
            display_hangman(tries)
            print(f'Загаданным словом было слово {word}')
        else:
            tries-=1
            c_c=0
            for c in guess:
                cnt=0
                if c in word:
                    c_c+=1    
                    guessed_letters.append(c)
                    while cnt!=word.count(c):
                        word_completition=word_completition[:(word.index(c))]+c+word_completition[(word.index(c)+1):]
                        cnt+=1
            else:
                print(display_hangman(tries))
                print(word_completition)
            if c_c==0:
                print('Ни одной буквы из этого слова нет в загаданном...')
                print(display_hangman(tries))
                print(word_completition)
                continue


    
def main():
    cnt=0
    while True:
        welcome(cnt)
        cnt+=1
        play(get_word())
        decision = input('Хотите сыграть ещё? Y/N: ')
        if decision.lower() not in 'yн':
            print('Хорошего денёчка!')
            return False
    


main()