import random

#ex 1
def get_words_from_file(file_name):  

    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
        words_list = content.split()
        return words_list

def get_random_sentence(sentence_length):
    words_list = get_words_from_file("DI-Bootcamp/Week3/Day6/ExerciseXP/words.txt")
    sentence_words = []
    for i in range(sentence_length):
        random_word = random.choice(words_list)
        sentence_words.append(random_word)

    sentence = " ".join(sentence_words)
    return sentence.lower()

def main():
    print("Th program generates a sentence from random words.")
    sentence_length = input("Please enter the desirable sentence length:")
    if sentence_length.isdigit() and int(sentence_length) >= 2 and int(sentence_length) <= 20:
        print(get_random_sentence(int(sentence_length)))
    else:
        print("The input is invalid")
    


main()