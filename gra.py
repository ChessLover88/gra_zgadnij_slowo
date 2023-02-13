import sys

no_of_tries = 5
word = "kamil"
used_letters = []
user_word = []

for _ in word:
    user_word.append("_")
#def get_number(prompt="podaj litere:", err_msg="tylko litery polskiego alfabetu", parse=str):
   # while True:
      #  try:
        #    out= parse(input(prompt))
        #except ValueError:
          #  print (err_msg)
        #else:
          #  return out

while True:
    letter = input("podaj literę: ")
    used_letters.append(letter)

    def find_indexes(word, letter):
        indexes = []

        for index, letter_in_word in enumerate(word):
            if letter == letter_in_word:
                indexes.append(index)
        return indexes

    def show_state_of_game():
        print()
        print(user_word)
        print("Pozostało prób:", no_of_tries)
        print("Użyte litery:", used_letters)
        print()



    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("nie ma takiej litery")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("koniec gry:(")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter


        if "".join(user_word) == word:
            print('Brawo! "' + word + '" to jest szukane słowo!')
            sys.exit(0)

    show_state_of_game()


