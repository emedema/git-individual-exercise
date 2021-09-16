# git-individual-exercise explanation

## Running the Program

The way the sorting algorithms have been implemented, when you run the file directly there is no output. Therefore, if no errors appear after running the code below in the terminal, it has been run successfully.

```
python3 git_exercise.py
```

However, there are specific inputs and outputs for each method.

### Inputs and Outputs for each Method

#### `sort_integer(array)`
As the header of the method suggests, this method takes an array of integers and returns a sorted array of integers.

#### `sort_string(string)`
This method takes in a string to sort and returns a sorted string.

#### `merge_sort_string(array)`
This is a helper method for the `sort_string` method. This takes in a character array and returns a sorted array of characters.

#### `merge(left_array, right_array)`
This is a helper method for the `sort_integer()` and `sort_string()` function. It takes the two halves of the array (`left_array` and `right_array`) and returns a sorted array.

## Running the Test Program

The test program has output that details if the tests have passed or not. To run the test program you run the code below in the terminal.

```
python3 git_exercise_test.py
```

If all tests pass the output is:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

### Tests

#### `test_sort_integer`
This tests to see if the integer sort functionality works. This creates an unsorted array and a sorted version of the same array. It then calls the `sort_integer` function and compares the now-sorted array and the originally sorted array to ensure that the function has sorted the array properly. If they are the same, the test passes.

#### `test_sort_integer_length`
This tests that if array is < 2 in length it gets returned as it is already sorted. It created an array with only one integer, then calls the `sort_integer` function. If the returned value is the same as the created array then the test passes.

#### `test_sort_string`
This tests to see if the string is sorting correctly. This creates an string that consists of a word and a sorted version of the same word. It then calls the `sort_string` function and compares the now-sorted string and the originally sorted word to ensure that the function has sorted the array properly. If they are the same, the test passes.

#### `test_sort_string_length`
This tests that if a string is < 2 characters in length it gets returned as it is already sorted. It created an string with only one character, then calls the `sort_string` function. If the returned value is the same as the created string then the test passes.
