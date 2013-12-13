#Python Pig Latin tran 
#input word
original = raw_input('Enter a word:')

#suffix for consonants
pyg = 'ay'

#find if there is an input and if its a string
if len(original) > 0 and original.isalpha():
    word = original.lower()   #turns input into lower case
    first = word[0]           #finds first letter of word
    new_word = word + pyg     #sets new word as as lower case + pyg
    
       #find vowel  
    if first in 'aeiou':      #better way to find vowels than 
        print new_word        # if first == a, first == e ... etc.
    else:                     #find consonant, if not vowel
        new_word = word[1:] + first + pyg   #sets new_word to
        print new_word                      #consonant form in 
                                            #pig latin
else:
    print 'Please enter a word'             #print if nothing is 
                                            #inputted