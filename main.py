HANGMAN_ASCII_ART = """Welcome to the game Hangman   
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \.
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/ 
                     
"""

MAX_TRIES = 6
MAX_TRIES = str(MAX_TRIES)
print(HANGMAN_ASCII_ART + MAX_TRIES )

def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {}
    HANGMAN_PHOTOS[1] = "    x-------x"
    HANGMAN_PHOTOS[2] = """    x-------x
    |
    |
    |
    |
    |"""
    HANGMAN_PHOTOS[3] = """    x-------x
    |       |
    |       0
    |
    |
    |"""
    HANGMAN_PHOTOS[4] = """"    x-------x
    |       |
    |       0
    |       |
    |
    |
    """
    HANGMAN_PHOTOS[5] = """"    x-------x
    |       |
    |       0
    |      /|\.
    |
    |"""
    HANGMAN_PHOTOS[6] = """    x-------x
    |       |
    |       0
    |      /|\.
    |      /
    |"""
    HANGMAN_PHOTOS[7] = """    x-------x
    |       |
    |       0
    |      /|\.
    |      / \.
    |"""
    return HANGMAN_PHOTOS[num_of_tries]

def choose_word(file_path, index):
    with open(file_path, 'r') as words:
        words_inf = words.read()
        words_list = words_inf.split(' ')
        if index > len(words_list):
            index = 1
        chosen_word = words_list[index - 1].replace('\n', '')
        return chosen_word

def check_win(secret_word, old_letters_guessed):
    secret_wordlen = len(secret_word)
    for trueletter in range(secret_wordlen):
        if secret_word[trueletter] in old_letters_guessed:
            return True
        return False
    secret_wordlen+1

def show_hidden_word(secret_word, old_letters_guessed):
    currect_guess = ['']
    for letter in secret_word:
        if letter in old_letters_guessed:
            currect_guess.append(letter + " ")
        else:
            currect_guess.append("_ ")
        result = ''.join(currect_guess)
    return result

def check_valid_input(letter_guessed, old_letters_guessed):
    length1 = len(letter_guessed)
    if (length1 > 1) or (not letter_guessed.isalpha()) or (old_letters_guessed.count(letter_guessed)==1 or old_letters_guessed.count(letter_guessed) > 1 ):
        return False
    else:
        if (length1 == 1) and (letter_guessed.isalpha() and (old_letters_guessed.count(letter_guessed) == 0)):
                return True

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    new_old = ' -> '.join(old_letters_guessed)
    length1 = len(letter_guessed)
    count = old_letters_guessed.count
    if (length1 > 1) or (not letter_guessed.isalpha()) or (old_letters_guessed.count(letter_guessed) == 1 or old_letters_guessed.count(letter_guessed) > 1):
     print( "X \n" + new_old)
     return False
    else:
        if(length1 == 1) and (letter_guessed.isalpha() and (old_letters_guessed.count(count) == 0)):
            old_letters_guessed.append(letter_guessed.lower())
            return True

def word_len(secret_word):
    return '_ ' * len(secret_word)

num_of_tries = 0

def main():
    global num_of_tries
    secret_word = choose_word(input(r"Please enter file path: ").lower(), int(input(r"Please enter index: ")))
    old_letters_guessed = []
    print('Lets start!')
    while num_of_tries < MAX_TRIES:
        try_update_letter_guessed(input('Enter a letter: '), old_letters_guessed, secret_word)
        show_hidden_word(secret_word, old_letters_guessed)
        game_status = check_win(secret_word, old_letters_guessed)
        if game_status:
            break
    if not game_status:
        print('GAME OVER!')


if __name__ == "__main__":
    main()





