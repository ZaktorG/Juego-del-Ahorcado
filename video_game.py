def read_file():
    word = []
    with open("./source/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            word.append(line.strip("\n"))
    return word

def run():
    read_file()  

if __name__ == "__main__":
    run()