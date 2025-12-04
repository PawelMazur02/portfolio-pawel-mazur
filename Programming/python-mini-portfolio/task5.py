import re

class Text:
    def __init__(self, text):
        self.__text = text

    @property
    def text(self):
        return self.__text

class TextProcessor:
    def __init__(self, text_obj):
        self.__text = text_obj

    def text_analysis(self):
        return Text_dict(self.__text.text)

class Text_dict:
    def __init__(self, text):
        self.__text = text
        self.__words = self.__count_and_sort_words()

    def __count_and_sort_words(self):
        clean_text = re.sub(r'[^\w\s]', '', self.__text)
        words = clean_text.split()
        word_dict = {}
        for word in words:
            word = word.lower()
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
        return dict(word_dict.items())

    def raport(self):
        for word, count in self.__words.items():
            print(f"'{word}': {count} wystąpień")




article = "To jest pierwsze zdanie. To jest drugie zdanie. To jest trzecie zdanie!"
text = Text(article)
processor = TextProcessor(text)
text_dict = processor.text_analysis()
text_dict.raport()
