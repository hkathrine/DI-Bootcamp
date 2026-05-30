import random
import json

json_string = """
{
    "company": {
        "name": "TechCorp",
        "employee": {
            "name": "Alex",
            "payable": {
                "salary": 5000,
                "currency": "USD"
            }
        }
    }
}
"""

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
    #ex 1
    print("Th program generates a sentence from random words.")
    sentence_length = input("Please enter the desirable sentence length:")
    if sentence_length.isdigit() and int(sentence_length) >= 2 and int(sentence_length) <= 20:
        print(get_random_sentence(int(sentence_length)))
    else:
        print("The input is invalid")
    #ex 2
    data = json.loads(json_string)
    current_salary = data["company"]["employee"]["payable"]["salary"]
    print(f"Current salary: {current_salary}")

    data["company"]["employee"]["birth_date"] = "1812-05-15"

    with open("modified_data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print("The file is saves as 'modified_data.json'")



main()


