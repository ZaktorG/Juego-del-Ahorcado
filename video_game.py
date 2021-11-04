import random

def random_word(word, word_size):
    number_random = random.randint(0, word_size) 
    print(str(word.get(number_random)))
    

def read_file():
    word = {}
    with open("./source/data.txt", "r", encoding="utf-8") as f:
        i = 0
        for line in f:
            word[i] = line.strip("\n")
            i += 1
    return word, i

def run():
    word, word_size = read_file()
    random_word(word, word_size)  

if __name__ == "__main__":
    run()