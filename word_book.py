import random

'''
Helper class to aid in getting dictionary terms from dict/words. Works only on Linux based os's for now
'''
class WordBook(object):
    def __init__(self):
        pass
    
    def generate_words(self, train=False):
        for word in filter(self.word_length_is_6, self.read_words(train)):
            yield word

    def read_words(self, train):
        if train:
            return open("/usr/share/dict/words").read().splitlines()
        else:
            return sorted(open("/usr/share/dict/words").read().splitlines(), key=lambda *args: random.random())
        
    def word_length_is_6(self, word):
        return len(word) == 6