# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    @property
    def word(self):
        return self._word
    
    @word.setter
    def word(self, value):
        if isinstance (value, str):
            self._word = value

        else:
            print("the anagram should be a string")

    def match(self, values):
        chosen_word = sorted(self.word)
        matched_words = []

        for value in values:
            if sorted(value) == chosen_word:
                matched_words.append(value)  

        return matched_words



listen = Anagram("angel")
listen.match(["baby", "hello", "glean"])



