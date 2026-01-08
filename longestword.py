def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest, len(longest)


 
words = ['welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey']

result = longest_word(words)

print("Longest word:", result[0])
print("Length:", result[1])



for(int counter = 1;counter < 5 ;counter++){
}


int count = 1;
while(count < 5 ){
count++


}
