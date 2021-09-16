import unittest

from git_exercise import sort_integer, sort_string

class TestSort(unittest.TestCase):

    def test_sort_integer(self):
        '''
        Tests to see if the integer sort functionality works
        '''
        sorted = [1, 2, 3, 4, 5]
        unsorted = [2, 5, 4, 1, 3]

        self.assertEqual(sorted, sort_integer(unsorted))
    
    def test_sort_integer_length(self):
        '''
        Test that if array is < 2 in length it gets returned
        '''
        array = [5]

        self.assertEqual(array, sort_integer(array))
    
    def test_sort_string(self):
        '''
        Test to see if the string is sorting correctly
        '''
        word = 'testing'
        sorted_word = 'eginstt'
        self.assertEqual(sorted_word, sort_string(word))
    
    def test_sort_string_length(self):
        '''
        Test that if a string is less than < 2 characters long it gets returned
        '''
        word = 't'
        self.assertEqual(word, sort_string(word))

if __name__ == "__main__":
     unittest.main()