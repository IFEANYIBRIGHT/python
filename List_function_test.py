import unittest
from List_of_numbers import TestLengthOfNumbers

class TestForAddition(unittest.TestCase):

    def test_for_random(self):
        numbers = [2,3,4,5,6,7,8,3]
        random_numbers_of_list = TestLengthOfNumbers()
        expected = random_numbers_of_list.length_of_numbers(numbers)
        actual = 8

        self.assertTrue(expected,actual)

 

    def test_even_numbers(self):
       numbers = [2,3,5,6,7,8,4]

       sum_even_positions = TestLengthOfNumbers()

       expected  = sum_even_positions.even_indexes(numbers)
       
       actual = 18
    
       self.assertEqual(expected,actual)

    
    def test_odd_numbers(self):
        numbers = [2,3,5,6,7,8,4] 

        sum_of_odd = TestLengthOfNumbers()

        expected = sum_of_odd.odd_indexes(numbers)

        actual = 17

        self.assertEqual(expected,actual)



    def test_multiply_for_third_numbers(self):
        numbers = [2,3,5,6,7,8,4] 

        multiple_of_numbers = TestLengthOfNumbers()

        expected = multiple_of_numbers.multiply_elements(numbers)

        actual = 24

        self.assertEqual(expected,actual)



    def test_average_of_numbers(self):
        numbers = [2,3,5,6,7,8,4]             

        average = TestLengthOfNumbers()

        expected = average.average_of_numbers(numbers)

        actual = 5.0
    
        self.assertEqual(expected,actual)  


    def test_largest_numbers(self):

        numbers = [2,3,4,5,6,7,8,6]

        largest  = TestLengthOfNumbers()
    
        expected = largest.largest_of_numbers(numbers)

        actual = 8

        self.assertEqual(expected,actual)



    
    def test_smallest_numbers(self):

        numbers = [2,3,4,5,6,7,8,6]

        smallest  = TestLengthOfNumbers()
    
        expected = smallest.smallest_of_numbers(numbers)

        actual = 2

        self.assertEqual(expected,actual)


    def test_if_string_first_and_last_characters(self):
        characters = "madam"
        
        character = TestLengthOfNumbers()
    
        expected = character.return_character(characters)

        actual = "madam"

        self.assertEqual(expected,actual)



    def test_if_list_is_in_sequence(self):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        list_of_numbers =  TestLengthOfNumbers()

        expected = list_of_numbers.sequential_integers(numbers)

        actual = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

        self.assertEqual(expected,actual)
                


    def test_if_all_third_elements_add(self):
        numbers = [2,3,4,4,6,7,8]

        third_elements = TestLengthOfNumbers()

        expected = third_elements.sequential_integers(numbers)

        actual = 12

        self.assertTrue(expected,actual)



    
    def test_if_it_calculates_first_middle_last_number(self):
        numbers = [2,3,4,4,6,7,8]

        elements = TestLengthOfNumbers()

        expected = elements.first_middle_last_elements(numbers)

        actual = 14.0

        self.assertTrue(expected,actual)






























