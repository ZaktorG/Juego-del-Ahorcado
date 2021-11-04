import os
import random

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

def random_word(word, word_size):
    number_random = random.randint(0, word_size) 
    return word.get(number_random)
    
def read_file():
    words = {}
    with open("./source/data.txt", "r", encoding="utf-8") as f:
        i = 0
        for line in f:
            words[i] = line.strip("\n")
            i += 1
    return words, i

def run():
    os.system("clear")
    choice_menu = input(TITLE_GAME)

    words, word_size = read_file()
    word_game = random_word(words, word_size)  

    if choice_menu == "1":
        pass 
    elif choice_menu == "2":
        pass 
    elif choice_menu == "3":
        pass 
    else:
        os.system("clear")
        choice_menu = input(TITLE_GAME_ERROR)
        

if __name__ == "__main__":
    run()