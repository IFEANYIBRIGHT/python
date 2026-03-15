import random

class TestLengthOfNumbers: 
    def random_numbers(num):
         for count in range(10):
            num = random.randint(1, 50)
            numbers.append(num)

         return numbers

 
    def length_of_numbers (self,number):
        count = 0
        for num in number:
            count += 1

        return count
 
    def even_indexes(self,numbers):  
        sum_of_num = 0
        for number in range(0,len(numbers) ,2):
            sum_of_num += numbers[number]
        return sum_of_num


    def odd_indexes(self,numbers):
        sum_of_num = 0
        for number in range(1,len(numbers) ,2):
            sum_of_num += numbers[number]
        return sum_of_num 
 
 
     

    def multiply_elements(self,numbers):
        multiply = 1
      
        for num in range (3,len(numbers),3):
            multiply *= numbers[num]

        return multiply


    def average_of_numbers(self,numbers):
        average = 0

        sum_of_numbers = 0

        for number in range(len(numbers)):
            sum_of_numbers += numbers[number]

            average = sum_of_numbers / len(numbers)
        return average
  

    def largest_of_numbers(self,numbers):
        largest = 0

        for number in range(len(numbers)):
            if numbers[number] > largest:
                largest = numbers[number]
        return largest


    def smallest_of_numbers(self,numbers):
        smallest = numbers[0]
        for number in numbers:
            if number < smallest:    
               smallest = number
        return smallest
 
    def return_character(self, string_character):
        if len(string_character) > 2 and string_character[0] == string_character[-1]:
            return string_character
        return None   
            

    def  sequential_integers(self,numbers):
         return numbers
 
 
    def add_every_third_elements(self,numbers):           
        sum_of_elements = 0
        for number in range(3,len(numbers),3):
            sum_of_elements += numbers[number]

        return sum_of_elements
            
 
    def first_middle_last_elements(self,numbers):
        middle = 0

        sum_of_all = 0
        
        for number in range(len(numbers)):
            middle = number // 2

            sum_of_all = numbers[0] + (numbers[middle -1] + numbers[middle] / 2) + numbers[-1]

        return sum_of_all
















#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
