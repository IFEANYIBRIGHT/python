def string_name(string_name)

string_name = input("Enter words")
length = len(string_name)
empty = ""

given_string = length[0] + length[1]+length[2] +length[-1] + length[-2]
print(given_string)
if(length < 2 )
    print(empty)
