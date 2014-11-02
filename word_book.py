class WordBook(object):
    def __init__(self):
        pass
    
    def generate_words(self, train=False):
        for word in filter(self.word_length_is_6, self.read_words()):
            yield word

    def read_words(self):
        return open("/usr/share/dict/words").read().splitlines()
        
    def word_length_is_6(self, word):
        return len(word) == 6