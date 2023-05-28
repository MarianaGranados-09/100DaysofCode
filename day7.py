#hang man game
import random

words = ["plate", "water", "table", "soup","dinosaur"]

chosen_word = random.choice(words)
#print(chosen_word)
print(f"The word has {len(chosen_word)} spaces!")
flag = 0
opport = 5
right_guesses = 0
while(flag == 0):
    guess = input("Please guess a letter: ")
    if guess in chosen_word:
        print(f"Great! You guessed the letter {guess} which is in position {chosen_word.find(guess) + 1}")
        right_guesses += 1
        if(right_guesses == len(chosen_word)):
            print(f"You won! The word was {chosen_word}")
            flag = 1
    else:
        opport =-1
        print(f"Wrong guess! Only {opport} more opportunities.")
        if opport == 0:
            print(f"Sorry, you lost. The word was {chosen_word}")
            flag = 1


