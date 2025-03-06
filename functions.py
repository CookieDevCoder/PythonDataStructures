# Brian Ayala
# Feb 25, 2025
# The purpose of this program is to demonstate data structures
# looping techniques, and enhanced Dictionary Operations in Python

def create_tuple(*args) :
    '''
    Pack the procided arguments into a tuple and return it
    Arguments: *args : A variable number of arguments
    Return: A tuple containing all the provided arguments
    '''
    return tuple(args)

def unpack_tuple(t = tuple()) :
    '''
    Description:
    Unpack the tuple into infividual variables and return them as a list.
    Arguments:
    t : A tuple to be unpacked
    Return:
    A list of the unpacked elements
    '''
    return list(t)

def tuple_details(t = tuple()) :
    '''
    Description:
    Return a dictionary containing details about the tuple such as length, the first element, and the last element
    Arguments:
    t : A tuple whose details are to be extracted
    Return :
    A dictionary with keys suck as 'length', 'first', and 'last'.
    '''
    length = len(t)
    firstElement = t[0]
    LastElement = t[length-1]
    return {'length' : length, 'first' : firstElement, 'last' : LastElement}

def create_set(iterable) :
    '''
    Description:
    Create a set from the given iterable.
    Arguments:
    iterable : An iterable from which to create a set.
    Return:
    A set containing unique elements from the iterable.
    '''
    return set(iterable)

def set_operations(s1, s2) :
    '''
    Description:
    Given two sets, perform various set operations and return the results in a dictionary.
    Arguments:
    s1 : The first set.
    s2 : The second set.
    Return:
    A dictionary with the following keys:
    - 'union' : The union of s1 and s2.
    - 'intersection' : The intersection of s1 and s2.
    - 'difference' : The difference (elements in s1 but not in s2).
    - 'symmetric_difference': The symmetric difference of s1 and s2.
    '''
    return {
        'union' : s1 | s2,
        'intersection' : s1 & s2,
        'difference' : s1 - s2,
        'symmetric_difference' : s1 ^ s1
        }

def unique_sorted (iterable) :
    '''
    Description:
    Return a sorted list of unique elements from the provided iterable.
    Arguments:
    iterable : An iterable that may contain duplicate elements.
    Return:
    A sorted list of the unique elements.
    '''
    return list(set(iterable))

def create_dictionary (pairs) :
    '''
    Description:
    Create a dictionary from a list of key-value pair tuples.
    Arguments:
    pairs : A list of tuples, where each tuple is a key-value pair.
    Return:
    A dictionary constructed from the provided pairs.
    '''
    return dict(pairs)

def update_dictionary (d, key, value) :
    '''
    Description:
    Update the dictionary with the provided key-value pair.
    If the key exists, its value is overwritten.
    Arguments:
    d : The dictionary to update.
    key : The key to update or add.
    value : The value associated with the key.
    Return:
    The updated dictionary.
    '''
    d[key] = value
    return d

def delete_key (d, key) :
    '''
    Description:
    Remove the specified key from the dictionary.
    If the key does not exist, return an error message or raise an exception.
    Arguments:
    d : The dictionary from which to delete a key.
    key : The key to be removed.
    Return:
    The dictionary after removal of the key, or an error message if the key is not found.
    '''
    if d.get(key) == None :
        return "Key does not exist"
    d.pop(key)
    return d

def dict_comprehension_example (iterable) :
    '''
    Description:
    Create a dictionary using comprehension that maps each element of the iterable
    to its square (if numeric) or its length (if a string).
    Arguments:
    iterable : An iterable containing numbers and/or strings.
    Return:
    A dictionary with each element as a key and its corresponding computed value.
    '''
    d = dict()
    for x in iterable :
        if type(x) == int :
            d[x] = x * x
        else :
            d[x] = len(x)
    
    return d


def merge_dictionaries (*dicts) :
    '''
    Description:
    Merge a list of dictionaries into a single dictionary.
    If the same key appears in multiple dictionaries, combine their values into a list.
    Arguments:
    dicts : A list of dictionaries to merge.
    Return:
    A dictionary where each key maps to a list of all values associated with that key from the input dictionaries.
    '''
    d = dict()

    for x in dicts :
        d.update(x)
    
    return d
    

def iterate_dictionary (d = dict()) :
    '''
    Description:
    Iterate over the dictionary and return a list of formatted strings showing key-value pairs.
    Arguments:
    d : The dictionary to iterate over.
    Return:
    A list of strings in the format "key: value".
    '''
    lst = list()
    for x in d.keys() :
        lst.append(x + ": " + d[x])
    
    return lst

def enumerate_list (lst = list()) :
    '''
    Description:
    Enumerate over the list and return a list of tuples containing the index and the corresponding element.
    Arguments:
    lst : The list to enumerate.
    Return:
    A list of tuples where each tuple is (index, element).
    '''
    tuplst = list()
    i = 0
    for x in lst :
        tuplst.append(tuple(i, x))
        i += 1
    
    return tuplst


def zip_lists (lst1 = list(), lst2 = list()) :
    '''
    Description:
    Pair elements from two lists using the zip function and return the resulting list of tuples.
    Arguments:
    lst1 : The first list.
    lst2 : The second list.
    Return:
    A list of tuples, each containing one element from lst1 and the corresponding element from lst2.
    '''
    tuplst = list()
    for x in range(0, len(lst1) - 1) :
        tuplst.append(tuple(lst1[x], lst2[x]))
    
    return tuplst

def reverse_and_sort (lst = list()) :
    '''
    Description:
    Return both a reversed version of the list and a sorted version of the list.
    Arguments:
    lst : The list to be processed.
    Return:
    A tuple with two lists:
    - The first is the reversed list.
    - The second is the sorted list.
    '''
    rlst = lst.reverse()
    slst = lst.sort()
    return tuple(rlst, slst)

def check_membership (sequence, value) :
    '''
    Description:
    Check if a value exists within a sequence.
    Arguments:
    sequence : The sequence to search.
    value : The value to check for.
    Return:
    True if the value is found, otherwise False.
    '''
    for x in sequence :
        if x == value :
            return True
        
    return False

def chained_comparison (a, b, c) :
    '''
    Description:
    Evaluate the chained comparison a < b == c and return the result.
    Arguments:
    a : The first value.
    b : The second value.
    c : The third value.
    Return:
    True if the comparison holds; otherwise, False.
    '''
    return a < b and b == c

def boolean_evaluation (a, b, c) : 
    '''
    Description:
    Evaluate the Boolean expression (a and not b) or c using short-circuit evaluation.
    Arguments:
    a : A Boolean or value evaluated in a Boolean context.
    b : A Boolean or value evaluated in a Boolean context.
    c : A Boolean or value evaluated in a Boolean context.
    Return:
    The result of the Boolean expression.
    '''
    return (a and not b) or c

def compare_sequences (seq1, seq2) :
    '''
    Description:
    Compare two sequences lexicographically.
    Arguments:
    seq1 : The first sequence.
    seq2 : The second sequence.
    Return:
    -1 if seq1 is less than seq2;
    0 if they are equal;
    1 if seq1 is greater than seq2.
    '''
    sseq1 = seq1.sort()
    sseq2 = seq2.sort()
    for x in range(0, len(seq1) - 1) :
        if sseq1[x] < sseq2[x] :
            return -1
        elif sseq2[x] < sseq1[x] :
            return 1
    
    return 0

def is_strictly_increasing (sequence) :
    '''
    Description:
    Check if a sequence of numbers is strictly increasing
    (i.e., each element is less than the next one).
    Arguments:
    sequence : A list or tuple of numbers.
    Return:
    True if the sequence is strictly increasing, otherwise False.
    '''
    max = sequence[0]
    for x in sequence :
        if x < max :
            return False
    
    return True