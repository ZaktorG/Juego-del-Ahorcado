import os
import random

from functools import reduce

TITLE_GAME = """       _                              _      _            _                             _       
      | |                            | |    | |     /\   | |                           | |      
      | |_   _  ___  __ _  ___     __| | ___| |    /  \  | |__   ___  _ __ ___ __ _  __| | ___  
  _   | | | | |/ _ \/ _` |/ _ \   / _` |/ _ \ |   / /\ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ 
 | |__| | |_| |  __/ (_| | (_) | | (_| |  __/ |  / ____ \| | | | (_) | | | (_| (_| | (_| | (_) |
  \____/ \__,_|\___|\__, |\___/   \__,_|\___|_| /_/    \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/ 
                     __/ |                                                                      
                    |___/                                                                       
                                     by Rodrigo Baez




[1] Jugar
[2] Reglas
[3] Salir

Ingrese su elección: """

TITLE_GAME_ERROR = """       _                              _      _            _                             _       
      | |                            | |    | |     /\   | |                           | |      
      | |_   _  ___  __ _  ___     __| | ___| |    /  \  | |__   ___  _ __ ___ __ _  __| | ___  
  _   | | | | |/ _ \/ _` |/ _ \   / _` |/ _ \ |   / /\ \ | '_ \ / _ \| '__/ __/ _` |/ _` |/ _ \ 
 | |__| | |_| |  __/ (_| | (_) | | (_| |  __/ |  / ____ \| | | | (_) | | | (_| (_| | (_| | (_) |
  \____/ \__,_|\___|\__, |\___/   \__,_|\___|_| /_/    \_\_| |_|\___/|_|  \___\__,_|\__,_|\___/ 
                     __/ |                                                                      
                    |___/                                                                       
                                     by Rodrigo Baez




[1] Jugar
[2] Reglas
[3] Salir

*Favor de ingresar una opción valida*
Ingrese su elección: """

WIN = """  
   ______                       __       ______
  / ____/___ _____  ____ ______/ /____  / / / /
 / / __/ __ `/ __ \/ __ `/ ___/ __/ _ \/ / / / 
/ /_/ / /_/ / / / / /_/ (__  ) /_/  __/_/_/_/  
\____/\__,_/_/ /_/\__,_/____/\__/\___(_|_|_)  


[1] Volver a Jugar
[2] Reglas
[3] Salir

Ingrese su elección: """

LOSE = """  
   ___             _ _     _         _  _  _ _
  / _ \___ _ __ __| (_)___| |_ ___  / \/ \/  / 
 / /_)/ _ \ '__/ _` | / __| __/ _ \/  /  /  /
/ ___/  __/ | | (_| | \__ \ ||  __/\_/\_/\_/ 
\/    \___|_|  \__,_|_|___/\__\___\/ \/ \/                                          
                                             
[1] Volver a Jugar
[2] Reglas
[3] Salir

Ingrese su elección: """

RULES = """* Tienes 10 vidas
* Tienes que encontrar la palabra
* Solo se puede una palabra a la vez
* Presionar Ctrl + C en juego y sera como si te hubieras rendido

[1] Volver a Jugar
[2] Reglas
[3] Salir

Ingrese su elección: """
def game(word_game, word_size):
    os.system("clear")
    vidas = 10
    word_game_result = ""
    words_input = []
    for i in range(word_size):
        words_input.append("_")
    
    while vidas > 0 and word_game != word_game_result:
        word_search = False
        print(str(vidas) + " vidas")
        for value in words_input:
            print(value, end=" ")
        try:
            word_input = input("\n\nIngrese una letra: ")
        except KeyboardInterrupt:
            break 
        for value in range(word_size):
            if word_input == word_game[value]:
                words_input[value] = word_input
                word_search = True
        if not word_search:
            vidas -= 1
        word_game_result = reduce(lambda a, b: a + b, words_input)
        os.system("clear")
    if word_game == word_game_result:
        return True
    else:
        return False

def random_word(word, words_size):
    number_random = random.randint(0, words_size) 
    word = word.get(number_random)

    word_size = 0
    for value in word:
        word_size += 1
    return  word, word_size

def normalize(word_game): 
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            word_game = word_game.replace(a, b).replace(a.upper(), b.upper())
        return word_game
    
def read_file():
    words = {}
    with open("./source/data.txt", "r", encoding="utf-8") as f:
        i = 0
        for line in f:
            words[i] = line.strip("\n")
            i += 1
    return words, i

def run():
    words, words_size = read_file()
    os.system("clear")
    try:
       choice_menu = input(TITLE_GAME)
    except KeyboardInterrupt:
        choice_menu = "3" 
    while choice_menu != "3":
        if choice_menu == "1":
            word_game, word_size = random_word(words, words_size) 
            if game(normalize(word_game), word_size):
                os.system("clear")
                try:
                    choice_menu = input(WIN)
                except KeyboardInterrupt:
                    choice_menu = "3" 
            else:
                os.system("clear")
                try:
                    choice_menu = input("La palabra era: " + word_game + LOSE)
                except KeyboardInterrupt:
                    choice_menu = "3" 
        elif choice_menu == "2":
            os.system("clear")
            try:
                choice_menu = input(RULES)
            except KeyboardInterrupt:
                choice_menu = "3" 
        elif choice_menu == "3":
            print("Bye") 
        else:
            os.system("clear")
            try:
                choice_menu = input(TITLE_GAME_ERROR)
            except KeyboardInterrupt:
                choice_menu = "3" 
        
if __name__ == "__main__":
    run()