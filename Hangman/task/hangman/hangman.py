import random


def hangman():
    tries = 8
    words = ('python', 'java', 'kotlin', 'javascript')
    word = random.choice(words)
    state = list(len(word) * '-')
    letters = set()

    while tries > 0:
        print()
        print(''.join(state))
        if '-' not in set(state):
            print("You guessed the word!", "You survived!", "", sep="\n")
            break
        letter = input("Input a letter:")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not letter.isalpha() or not letter.islower():
            print("It is not an ASCII lowercase letter")
        elif letter in letters:
            print("You already typed this letter")
        elif letter in set(word):
            state = [el if el == letter else state[i] for i, el in enumerate(word)]
        else:
            tries -= 1
            print("No such letter in the word")
        letters.add(letter)
    else:
        print("You are hanged!")


print("H A N G M A N")
while True:
    is_replay = input('Type "play" to play the game, "exit" to quit:')
    if is_replay == "play":
        hangman()
    elif is_replay == "exit":
        break
