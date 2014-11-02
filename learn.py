from profile_data import ProfileData, DataPoint, Profiles
from word_book import WordBook
import Levenshtein
import time
import curses


class CursesMixin(object):
    #function used to read the characters from the command line using ncurses
    def read_char(self, stdscr):
        curses.noecho()
        backspace_count = 0
        word = ""
        cursor_location = stdscr.getyx()
        while 1:
            c = stdscr.getch()
            stdscr.move(cursor_location[0], cursor_location[1])
            if c == curses.KEY_BACKSPACE or c==127:
                backspace_count += 1
                word = word[:-1]
                stdscr.addstr(word)
                stdscr.clrtobot()
            elif c == curses.KEY_ENTER or c==10:
                break
            else:
                word += str(unichr(c))
                stdscr.addstr(word)
            
        return (backspace_count, word)

class Learn(CursesMixin):
    def __init__(self, stdscr):
        wordbook = WordBook()
        stdscr.addstr("What is your name?")
        profile_data = ProfileData()
        profiles = Profiles()
        profiles.append_profile(ProfileData)
        stdscr.refresh()
        name = stdscr.getstr(1,0, 15)
        profile_data.set_name(name)
        stdscr.clear()
        
        #iterate over every word in the dictionary forever until the user enters nothing
        for word in wordbook.generate_words(train=True):
            stdscr.addstr(0,0, "%s" % (" " * 100))
            stdscr.addstr(0,0, "-> %s " % (word))
            stdscr.refresh()
            start = time.time()
            count, user_word = self.read_char(stdscr)
            end = time.time()
    
            stdscr.addstr(3, 0, "Time taken: %i, times_corrected: %i" % (end-start, count))
    
            if user_word == "":
                break

            #create a data point with the Levenshtein distance, 
            #count of errors user made while typing, and how long the process took 
            data_point = DataPoint(time=end-start, error_count=count, distance=Levenshtein.distance(word, user_word))
            profile_data.append_point(data_point)
            profiles.flush()