class WordBook(object):
    def __init__(self):
        pass
    
    def generate_words(self):
        for word in filter(self.word_length_more_than_5, self.read_words()):
            yield word

    def read_words(self):
        return open("/usr/share/dict/words").read().splitlines()
        
    def word_length_more_than_5(self, word):
        return len(word) > 6