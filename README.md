# git-individual-exercise
A simple impementation of some sorting algorithms.

## Features

### integer-sort

Integer sorting sorts an array of numbers from smallest to largest. This is implemented via the merge sort algorithm.

In order to use this feature, we first create an object of the class `sort` which takes an array as the input:

```
sort = Sort([2, 5, 4, 3, 1])
```

Then we can use the `integer_sort` function (defined below) to sort the array.

```
sorted = sort.integer_sort()
```

## Methods

### `integer_sort()`
This function is the main controller of the integer-sort feature. It utilizes recursion to call itself on each half of the array created and then calls upon the `merge()` helper method to join them.

### `merge(left, right)`
This is a helper method for the `integer_sort()` function. It takes the two halves of the array, sorts them and then combines them into a single sorted array which it returns.
