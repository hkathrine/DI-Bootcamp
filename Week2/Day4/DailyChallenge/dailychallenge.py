#1
string = input("please enter a string")
list = [word.strip() for word in string.split(",")]

sorted_list = sorted(list)

for i in range(len(sorted_list)):
    print(f"{sorted_list[i]}", end="")
    if i < len(sorted_list) - 1:
        print(",", end="")

print("\n")

#2
def longest_word(sentence):
    words = sentence.split(" ")
    max_len_idx = 0
    for i in range(len(words)):
        length_i = len(words[i])
        length_max = len(words[max_len_idx])
        if length_i > length_max:
            max_len_idx = i
    return words[max_len_idx]


longest_word("Margaret's toy is a pretty doll.")
longest_word("A thing of beauty is a joy forever.")
longest_word("Forgwtfullness is by all means powerless!")