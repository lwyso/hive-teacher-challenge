#Use this file of common words to write a program to find anagrams of words entered by a user.

#e.g.
#$ python3 anagrammer.py
#Enter a word: race

#Anagrams of 'race' are:
#acer
#care

wordlist = open('wordlist.txt', 'r')

word = input('Enter a word: ')


#wordsplit = list(word)

print(word)
print(len(word))

def Newlist(word, wordlist):
	newlist = []
	for w in wordlist:
		w = w.strip()
		if len(w) == len(word) and sorted(w) == sorted(word):
			newlist.append(w)
	return newlist

finallist = Newlist(word, wordlist)
print(finallist)
