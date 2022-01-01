#importing words
import nltk
nltk.download('words')
from nltk.corpus import words
word_list = words.words()

#asking for input
letters_string = input("ENTER YOUR LETTERS IN LOWER CASE WITH NO SPACES INBETWEEN. GETS SLOW AT TEN: ")

#creating a list, where each element is a singular letter
letters_list = []
for i in range(0,len(letters_string)): # for i in letters_string
    letters_list.append(letters_string[i])

#creating a list where each element is a string with a different combination of initial letters
perms = []
import itertools
for x in itertools.permutations(letters_list):
    y = ''.join(x)
    perms.append(y)

#shortening the length
diff_lengths = []
for a in range(0,len(perms)):
    for i in range(0,len(letters_string)):
            diff_lengths.append((perms[a])[0:i+1])

#Removing duplicates and one letter words
diff_lengths = set(diff_lengths)
diff_lengths = [i for i in diff_lengths if len(i) > 1]

#checking if it matches with word_list
set_diff_lengths = set(diff_lengths)
set_word_list = set(word_list)
final = set_diff_lengths.intersection(set_word_list)
print(final)
