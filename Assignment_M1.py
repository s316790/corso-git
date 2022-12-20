# M1_A1: OK
input_word = input('Write a word: ')

vowels = ['a','e','i','o','u']

prefix = ['b','c','d','f']

cont = 0
condition = False

for x in input_word:
    for y in vowels:
        if x == y and cont != 0:
            suffix = input_word[cont:]
            condition = True
            break
    cont += 1
    if condition == True:
        break
    
cont = 0
rhyme_word = []

for x in range(len(prefix)):
    rhyme_word.append(prefix[cont] + suffix) 
    cont += 1

print(rhyme_word)