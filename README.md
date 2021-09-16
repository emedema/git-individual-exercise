# git-individual-exercise
A simple impementation of some sorting algorithms.

## Features

### integer_sort

Integer sorting sorts an array of numbers from smallest to largest. This is implemented via the merge sort algorithm.

First we must create an unsorted array.

```
array = [2, 5, 4, 1, 3]
```

Then we can use the `sort_integer` function (defined below) to sort the array.

```
sorted = sort_integer(array)
```

### string_sort

String sorting sorts a string from first in the alphabet to last in the alphabet.

**Note:** The string sort algorithm converts all strings to lowercase and only returns lowercase strings.


| Before | After |
| --- | ----------- |
| testing | eginstt |


This is implemented via merge sort.

In order to use the `sort_string` function (defined below) we first create a string consisting of a word.

```
word = "testing"
```

Then we can call the function

```
sorted_word = sort_string(word)
```

## Methods

### `sort_integer(array)`
This function is the main controller of the integer_sort feature. It utilizes recursion to call itself on each half of the array created and then calls upon the `merge()` helper method to join them. Eventually, it returns a sorted array.

### `merge(left, right)`
This is a helper method for the `sort_integer()` and `sort_string()` function. It takes the two halves of the array, sorts them and then combines them into a single sorted array which it returns.

### `sort_string(word)`
This function is the initial function of the `string_sort` feature. It relies on two separate methods, `merge_sort_string()` and `merge()`, however, it also splits up the word into a character array which allows us to sort it and it combines the returned sorted array back into a string before returning the sorted word.

### `merge_sort_string(array)`
This is a helper method for the `sort_string()` function. It utilizes recursion to call itself on each half of the array created and then calls upon the `merge()` helper method to join them. Eventually, it returns a sorted array of characters.
