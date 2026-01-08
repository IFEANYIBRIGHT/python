
string_word = input("Enter words :")
word = "ing"
words = "ly"
 
less_than = ""
length = len(string_word)
if(string_word.endswith(word)):
    print(string_word,words)

if(length == 3):
    print(string_word,word)
elif(length > 3):
    print(string_word ,word)
else :
    print(less_than)

