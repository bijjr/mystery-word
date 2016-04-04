import random

def easy_words(word_list):
    #
    return [word for word in word_list if len(word) >= 4 and len(word) <= 6]

def medium_words(word_list):
    #
    return [word for word in word_list if len(word) >= 6 and len(word) <= 8]

def hard_words(word_list):
    #
    return [word for word in word_list if len(word) >= 8]

def random_word(word_list):
    #
    return random.choice(word_list).lower()

def display_word(answer, guesses = []):
    displayword = ''
    for char in answer:
        if char in guesses:
            displayword += char + ' '
        else:
            displayword += '_ '
    return displayword.upper().rstrip()

def correct_guess(answer,guesses, chances):
    displayword = display_word(answer, guesses)
    if is_word_complete(answer,guesses):
        play_again()
    else:
        print("HIT!")
        print("Letters guessed: {}".format(guesses))
        print(displayword)
    return guesses

def incorrect_guess(chances,guesses,answer):
    displayword = display_word(answer,guesses)
    if guesses[-1].isalpha():
        chances -= 1
        if chances == 0:
            print('You lost')
            print('{} was the word'.format(answer.upper()))
            return play_again()
        else:
            print("MISS! You have {} guesses left".format(chances))
            print("Letters guessed: {}".format(guesses))
            #Displays visualization for word
            print(displayword)
            #Apart of the recursive chain, returns back to x function
            return chances
    else:
        print('Enter a letter')
        return chances

def game_flow(answer):
    guesses = []
    chances = 8
    while chances > 0:
        guess = user_guess()
        if guess == 'help':
            helper()
        elif guess == 'quit':
            return quit()

        elif guess in guesses:
            print("Already guessed that character")
        elif len(str(guess)) > 1:
            print("One letter only")

        elif guess in list(answer):
            guesses.append(guess)
            guesses = correct_guess(answer, guesses, chances)

        else:
            guesses.append(guess)
            chances = incorrect_guess(chances, guesses, answer)

    play_again()

def user_guess():
    guess = input("Letter? ").lower()
    if not guess.isalpha():
        print("Letters only")
        user_guess()
    else:
        return str(guess)

def main():
    #Opens file
    with open('/usr/share/dict/words') as file:
        #creates list, word_list, and splits words
        word_list = file.read().split()
        #print word_list
    print("""
    type 'Help' for instructions
    type 'Quit' to leave the game
    """)
    try:
        difficulty = int(input("""
        Pick a level of difficulty:

        Easy Mode? (4 - 6 Characters) - Press '1'
        Normal Mode? (6 - 8 Characters) - Press '2'
        Hard Mode? (8+ Characters) - Press '3'
        """))
    except:
        print("1, 2, or 3 only")
        return main()

    if difficulty == 1:
        answer = random_word(easy_words(word_list))
    elif difficulty == 2:
        answer = random_word(medium_words(word_list))
    elif difficulty == 3:
        answer = random_word(hard_words(word_list))
    else:
        print("1, 2, or 3. No letters")
        return main()

    game_flow(answer)

def helper():
    print("""
    You have 8 chances to guess the word
    If you run out of guesses you lose.

    Type 'Help' for this message
    Type 'Quit' to exit the game
    """)

def is_word_complete(answer, guesses):
    displayword = display_word(answer, guesses)
    if '_' not in displayword:
        print(displayword)
        print("You Win!")
        return True

def play_again():
    print("Would you like to play again?")
    play = int(input("""
    1.Yes
    2. No
    >
    """))
    if play == int(1):
        main()
    else:
        exit()

if __name__ == '__main__':
    main()
