import random

for index in range(10):

    random_numbers = random.randint(1,51)

    print(random_numbers)

print()

numbers = [23,34,5,6,7,8,5,4,3,2]

count = 0

average = 0

multiply = 1

sum_of_all = 0

average = 0 

number_of_strings = 0

smallest = numbers[0]

largest = numbers[0]

for index in range(len(numbers)):

    count += 1
    
    
print("The length is",count)    
 
print(numbers[: : 2])

 
print( numbers[ 1: : 2])

print()

for index in range(3,len(numbers),3):

    multiply *= index
    
    
print(multiply)    

print()

for index in range(len(numbers)):

    sum_of_all += index
    
average =    sum_of_all / len(numbers) 


print("The Average of all numbers in a list is ",average) 

print()

for index in range(len(numbers)):

    if index > largest:
    
        largest = index
        
print(largest)        
        
print(min(numbers)) 
      
print()
       
def first_and_last_character(character):

    if len(character) > 2 and character[0] == character[-1]:
        return character
    return "no same"

print(first_and_last_character("man"))   

print(first_and_last_character("madam"))  

print()


numbers = list(range(1, 16))

print(numbers)


def sum_every_third(intergers):
    return sum(intergers[::3])

 
numbers = list(range(1, 16))

print(sum_every_third(numbers))

print()

def sum_first_middle_last(number):

    first = number[0]

    middle = number[len(number) // 2]

    last = number[-1]

    
    return first + middle + last

 
numbers = list(range(1, 16))
print(sum_first_middle_last(numbers))





