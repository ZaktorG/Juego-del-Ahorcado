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
def game(word_game, word_size):
    os.system("clear")
    # print(word_game)
    vidas = 5
    word_game_result = ""
    words_input = []
    for i in range(word_size):
        words_input.append("_")
    
    while vidas > 0 and word_game != word_game_result:
        word_search = False
        word_input = input("Ingrese una letra: ")
        for value in range(word_size):
            if word_input == word_game[value]:
                words_input[value] = word_input
                word_search = True
        if not word_search:
            vidas -= 1
        # Solo falta reducir la palabra a un solo string para comparar
        word_game_result = reduce(lambda a, b: a + b, words_input)
        print(words_input, vidas, word_game_result)
    if word_game == word_game:
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
    choice_menu = input(TITLE_GAME) 
    while choice_menu != "3":
        if choice_menu == "1":
            word_game, word_size = random_word(words, words_size) 
            if game(word_game, word_size):
                os.system("clear")
                print("Ganaste")
            choice_menu = input("\nstop")
        elif choice_menu == "2":
            pass 
        elif choice_menu == "3":
            pass 
        else:
            os.system("clear")
            choice_menu = input(TITLE_GAME_ERROR)
        

if __name__ == "__main__":
    run()