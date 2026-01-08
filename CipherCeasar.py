mode = input("Encrypt or Decrypt? ").lower()
text = input("Enter text: ")
shift = int(input("Enter shift: "))

shift %= 26
result = ""

for letter in text:
    if 'A' <= letter <= 'Z':
        position = ord(letter) - ord('A')
        new_position = position + shift  
   if mode == "encrypt":
     else position - shift:
        result += chr(new_position % 26 + ord('A'))

    elif 'a' <= letter <= 'z':
        position = ord(letter) - ord('a')
        new_position = position + shift 
    if mode == "encrypt" :
    else position - shift:
        result += chr(new_position % 26 + ord('a'))

    else:
        result += letter

print("Result:", result)

