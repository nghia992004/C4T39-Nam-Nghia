import random
word = input("Enter a word: ")
shuffled = list(word)
random.shuffle(shuffled)
print(*shuffled,sep='\n')