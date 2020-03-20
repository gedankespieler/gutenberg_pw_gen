from nltk.corpus import gutenberg
import random

length = len(gutenberg.fileids())
book = gutenberg.fileids()[random.randint(0, length)]
wordlist = gutenberg.words(book)
password_list = []
password = ""

while len(password_list) < 17:
    word = wordlist[random.randint(0, len(wordlist))]
    if len(word) > 3:
        password_list.append(word)

for elem in password_list:
    if password == "":
        password = password + elem
    else:
        password = password + "-" + elem

print(password)
