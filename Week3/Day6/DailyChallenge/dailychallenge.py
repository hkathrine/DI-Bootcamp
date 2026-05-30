
class Text:
    def __init__(self, text):
        self.text = text
    @classmethod
    def from_file(cls, file_path):
        
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return cls(content)


    def _get_clean_words(self):
        cleaned_text = self.text.lower()
        for char in [".", ",", "!", "?", ";", ":"]:
            cleaned_text = cleaned_text.replace(char, "")
        return cleaned_text.split()
    def word_frequency(self, word):
        words_list = self._get_clean_words()
        target_word = word.lower()
        
        count = words_list.count(target_word)
        
        # if the word is found more than 0 times
        if count > 0:
            return count
        else:
            return f"the word '{word}' not found"
        
    def most_common_word(self):
        words_list = self._get_clean_words()
        if not words_list:
            return "No text."
            
        frequency_dict = {}
        for word in words_list:
            if word in frequency_dict:
                frequency_dict[word] += 1
            else:
                frequency_dict[word] = 1
                
        
        most_common = max(frequency_dict, key=frequency_dict.get)
        return most_common

    def unique_words(self):
        words_list = self._get_clean_words()
        
        unique_set = set(words_list)
        
        return list(unique_set)
    
def main():
    analyzer = Text.from_file("DI-Bootcamp/Week3/Day6/DailyChallenge/text.txt")

    # Теперь у объекта analyzer есть доступ ко всем методам из Part I:
    print("Unique words:", analyzer.unique_words())
    print("the most common word:", analyzer.most_common_word())


main()