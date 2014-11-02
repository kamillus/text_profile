from learn import Learn
import argparse
import curses

#the only extra argument is "learn" which is used to train the svm
parser = argparse.ArgumentParser(description='Recognize who is typing')
parser.add_argument('learn', help='teach the algorithm to recognize the user')

args = parser.parse_args()
stdscr = curses.initscr()


#need to know the name of the user for predictive purposes
if args.learn:
    learn = Learn(stdscr)