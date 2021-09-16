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

## Methods

### `sort_integer()`
This function is the main controller of the integer_sort feature. It utilizes recursion to call itself on each half of the array created and then calls upon the `merge()` helper method to join them.

### `merge(left, right)`
This is a helper method for the `sort_integer()` function. It takes the two halves of the array, sorts them and then combines them into a single sorted array which it returns.
