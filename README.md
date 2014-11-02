Text Profile
============

Get the user's text profile using concepts of machine learning based on their writing style.

Requirements
----

The app requires Python 2.7 and the following packages:

* scikit-learn==0.15.2
* scipy==0.14.0
* numpy==1.9.0
* python-Levenshtein==0.11.2

Learning
----

The first step is to teach the svm to recognize the user. I used about 15 data points for each user, but obviously, the more the better. To run the learning algorithm type:

`python word_game.py --learn`

The game will ask you for your name, and then will print out words that you have to retype on the screen. Don't try to race, do it as naturally as possible.

Once you feel you've entered enough words, just leave a word blank and press enter. Repeat for multiple users (You need at least 2 to classify properly)

Classifiying
----

Once you've gone through the learning step, the svm can now guess who's typing at the command line. Run the following to guess the user:

`python word_game.py`

You will be asked to enter a random word, after which, you will be given the best estimate of who's typing. Neat, huh?
