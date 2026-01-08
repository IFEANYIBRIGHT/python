import math

pizza = print("""

PIZZA TYPE              NUMBER OF SLICES                PRICE PER BOX
-----------------|------------------------------|----------------------------------
1: SAPA SIZE                                    |   5,000
                 |        8                     |
-----------------|------------------------------|----------------------------------
2: SMALL MONEY            10                    |   6,000
                 |                              |
-----------------|------------------------------|----------------------------------
3: YAHOO BOYS            16                     |   15,000
                 |                              |
-----------------|------------------------------|---------------------------------
4: HUNGRY MAN SIZE        22                    |   23,500
                 |                              |
-----------------|------------------------------|----------------------------------
""")
pizza =  input("place ur order:"). upper()

match(pizza):
      case "SAPA SIZE":
             price = 5000
             number_of_slices = 8      
        
      case "SMALL MONEY":
            price = 6000
            number_of_slices = 10

      case "YAHOO BOYS":
            price = 15000
            number_of_slices = 16

      case "HUNGRY MAN SIZE":
            price = 23000
            number_of_slices = 22
d
      case _:
            print("invalid input selected")
            exit()
                


number_of_people = int(input("Enter number of people "))

number_of_box =  math.ceil( number_of_people /  number_of_slices)

slices_altogether =  number_of_box * number_of_slices - number_of_people

total_prices_of_pizza = number_of_box * price


print(f"Number of boxes efficient for everyone is {number_of_box } boxes")
print(f"Number of slices remaining after partying is {slices_altogether } slices") 
print(f"The price is ${total_prices_of_pizza } ")











 





























































































