'''
COSC 499 Individual Git Assignment
Created by: Emily Medema | 91175448
'''

def merge(left, right):
    '''
    A helper function for sorting an integer area with merge sort.
    Code to merge two different arrays
    '''
    if len(left) == 0:
        #left array is empty, no need to merge
        return right
    
    if len(right) == 0:
        #right array is empty, no need to merge
        return left

    result = []
    i_left = i_right = 0

    #iterate through both arrays until all the elements are in the result array
    while len(result) < len(left) + len(right):
        #compare elements in left and right to sort them
        if left[i_left] <= right[i_right]:
            result.append(left[i_left])
            i_left += 1
        else:
            result.append(right[i_right])
            i_right += 1
        
        #if there are any elements left of either array, add them to the end
        if i_right == len(right):
            result += left[i_left:]
            break
        
        if i_left == len(left):
            result += right[i_right:]
            break
    
    return result


def sort_integer(array):
    '''
    Implementation of sorting an integer array via merge sort
    '''

    if len(array) < 2:
        #already sorted
        return array

    #split array
    middle = len(array) // 2

    return merge(
                left = sort_integer(array[:middle]),
                right = sort_integer(array[middle:]))

def sort_string(word):
    '''
    Implementation of sorting a string via merge sort
    '''
    #split word into a character array
    chars = list(word.lower())
    result = ""

    #now that we have a array of characters, we can use merge sort
    sorted_chars = merge_sort_string(chars)
    #join characters back into string
    return result.join(sorted_chars)


def merge_sort_string(array):

    if len(array) < 2:
        #already sorted
        return array

    #split array
    middle = len(array) // 2

    #return with recursive calls
    return merge(
                left = sort_integer(array[:middle]),
                right = sort_integer(array[middle:]))