card_number= input("Kindly Enter Ur Card Number To Be Verified: ")
length = len(card_number)
sumOfEven = 0
sumOfOdd = 0
cardType = "invalid card"
cardValidity = "Not valid"

for counter in range (lengthOfCreditCard -2, 0,-2 ):
    digit =int(credit_Card[counter]) 

    digit *= 2

if digit > 9 :
   digit -= 9
   sumOfEven + digit
 

for index in range (lengthOfCreditCard -1 ,0,-2):

    number = int(credit_Card[index])
    number *= 2
    sumOfOdd += sumOfEven
if number % 10 == 0:
   card_Validity = "valid"

if(cardValidity == "Valid"):
    print("Card is valid")

if(creditCard.startsWith ("4")):
    cardType =  "Visa Card"
elif(creditCard.startsWith ("5")):
    cardType = "Master Card"
elif(creditCard.startsWith ("6")):
    cardType = "Discover Card"

elif ((creditCard.startsWith ("34") or creditCard. startsWith("37")) 
         and creditCard.length() == 15):
    cardType = "American Express Card"

else:
 print("Invalid input")


print("Card Number :" ,creditCard )

print("Card length :",lengthOfCreditCard )

print("Card Type :" ,cardType)

print("Card validity :" , cardValidity)





















    














