# Name: Brian Ayala
# Date: Feb 25, 2025
# The purpose of this program is to demonstate data structures
# looping techniques, and enhanced Dictionary Operations in Python

from functions import (
    create_tuple,
    unpack_tuple,
    tuple_details,
    create_set,
    set_operations,
    unique_sorted,
    create_dictionary,
    update_dictionary,
    delete_key,
    dict_comprehension_example,
    iterate_dictionary,
    enumerate_list,
    zip_lists,
    reverse_and_sort,
    check_membership,
    chained_comparison,
    boolean_evaluation,
    compare_sequences
)

# Creates a tuple (3, 6, 2, 2, 5)
testtuple = create_tuple(3, 6, 2, 2, 5)
print("Created Tuple: " + str(testtuple) + " | Passed = " + str(testtuple == tuple((3, 6, 2, 2, 5))))

# Creates a list [3, 6, 2, 2, 5]
testlst = unpack_tuple(testtuple)
print("Created List: " + str(testlst) + " | Passed = " + str(testlst == [3, 6, 2, 2, 5]))

# Creates a Dict with length = 5, First = 3, Last = 5
tupledetails = tuple_details(testtuple)
print("Tuple Details: " + str(tupledetails) + " | Passed = " + str(tupledetails == {'length' : 5, 'first' : 3, 'last' : 5}))

# Test Case: Empty Tuple
# Creates a Dict with length = 0, First = None, Last = None
emptydetails = tuple_details(tuple())
print("Empty Tuple Details: " + str(emptydetails) + " | Passed = " + str(emptydetails == {'length' : 0, 'first' : None, 'last' : None}))

# Create a set {7, 2, 3, 4, 1}
testset = create_set([7, 2, 3, 4, 1, 3])
print("Created Set: " + str(testset) + " | Passed = " + str(testset == {7, 2, 3, 4, 1}))


# Set Operations
testset2 = {3, 2, 5, 1, 6}
setopdict = set_operations(testset, testset2)

# Union == {7, 2, 3, 4, 1, 5, 6}
print("Set Union: " + str(setopdict['union']) + " | Passed = " + str(setopdict['union'] == {7, 2, 3, 4, 1, 5, 6}))
# Intersection = {2, 3, 1}
print("Set Intersection: " + str(setopdict['intersection']) + " | Passed = " + str(setopdict['intersection'] == {2, 3, 1}))
# Difference
print("Set Difference: " + str(setopdict['difference']) + " | Passed = " + str(setopdict['difference'] == {4, 7}))
# Symmetrical Difference
print("Set Symmetrical Difference: " + str(setopdict['symmetric_difference']) + " | Passed = " + str(setopdict['symmetric_difference'] == set()))

# Create list from [3, 6, 2, 2, 5] to [2, 3, 5, 6]
uniquelst = unique_sorted(testlst)
print("Unique Sorted testlst: " + str(uniquelst) + " | Passed = " + str(uniquelst == [2, 3, 5, 6]))

# Create Dictionary { 'Name' : "Brian", 'Age' : 19, 'Major' : "Computer Science"}
personinfo = create_dictionary(tuple((('Name', "Brian"), ('Age', 19), ('Major', "Computer Science"))))
print("Created personal info Dictionary: " + str(personinfo) + " | Passed = " + str(personinfo == { 'Name' : "Brian", 'Age' : 19, 'Major' : "Computer Science"}))

# Update person Info from age 19 to age 20 'Age' = "20"
updatedpersoninfo = update_dictionary(personinfo, 'Age', "20")
print("Created personal info Dictionary: " + str(updatedpersoninfo) + " | Passed = " + str(updatedpersoninfo == { 'Name' : "Brian", 'Age' : 20, 'Major' : "Computer Science"}))

# Delete Age from person Info
deletedpersoninfo = delete_key(updatedpersoninfo, 'Age')
print("Created personal info Dictionary: " + str(deletedpersoninfo) + " | Passed = " + str(deletedpersoninfo == { 'Name' : "Brian", 'Major' : "Computer Science"}))

# Test Case: Delete 'University', which does not exist
try :
    deleteunipersoninfo = delete_key(deletedpersoninfo, 'University')
except KeyError :
    print("Error was sucessfully Detected, University key was not deleted")

# Convert list [2, 7, "Hello", 3, "World"] to { 2 : 4, 7 : 49, "Hello" : 5, 3 : 9, "World" : 5}
dictcomprehension = dict_comprehension_example([2, 7, "Hello", 3, "World"])
print("Created personal info Dictionary: " + str(dictcomprehension) + " | Passed = " + str(dictcomprehension == { 2 : 4, 7 : 49, "Hello" : 5, 3 : 9, "World" : 5}))

# Format person into to list of strings conatining ["Name: Brian", "Major: Computer Science"]
listdicts = iterate_dictionary(deletedpersoninfo)
print("Merged Dictionaries: " + str(listdicts) + " | Passed = " + str(listdicts == ["Name: Brian", "Major: Computer Science"]))

# Convert testlst to [(1, 3), (2, 6), (3, 2), (4, 2), (5, 5)]
numberedtestlst = enumerate_list(testlst)
print("Enumerate List: " + str(numberedtestlst) + " | Passed = " + str(numberedtestlst == [(1, 3), (2, 6), (3, 2), (4, 2), (5, 5)]))

# Convert ["One", "Two", "Three"] and [1, 2, 3] to [("One", 1), ("Two", 2), ("Three", 3)]
NumbersList = zip_lists(["One", "Two", "Three"], [1, 2, 3])
print("Zip List : " + str(NumbersList) + " | Passed = " + str(NumbersList == [("One", 1), ("Two", 2), ("Three", 3)]))

# Set reversetestlst to [5, 2, 2, 6, 3] and sortedtestlst to [2, 2, 3, 5, 6]
reversetestlst, sortedtestlst = reverse_and_sort(testlst)
print("Reverse List : " + str(reversetestlst) + " | Passed = " + str(reversetestlst == [5, 2, 2, 6, 3]))
print("Sorted List : " + str(sortedtestlst) + " | Passed = " + str(sortedtestlst == [2, 2, 3, 5, 6]))

# Check if 5 is in testlst, it is (True)
contains5 = check_membership(testlst, 5)
print("testList Contains 5? : " + str(contains5) + " | Passed = " + str(contains5 == True))

# Check if 4 is in testlst, it is not (False)
contains4 = check_membership(testlst, 4)
print("testList Contains 4? : " + str(contains4) + " | Passed = " + str(contains4 == False))

# Checks if 1 < 2 == 2 (True)
is1lessthan2andequal2 = chained_comparison(1, 2, 2)
print("1 < 2 == 2 : " + str(is1lessthan2andequal2) + " | Passed = " + str(is1lessthan2andequal2 == True))

# Checks if 1 < 2 == 3 (False)
is1lessthan2andequal3 = chained_comparison(1, 2, 3)
print("1 < 2 == 2 : " + str(is1lessthan2andequal3) + " | Passed = " + str(is1lessthan2andequal3 == False))

# Evaluate (False and not True) or True (True)
truec = boolean_evaluation(False, True, True)
print("(False and not true) or True : " + str(truec) + " | Passed = " + str(truec == True))

# Evaluate (True and not True) or False (False)
falseab = boolean_evaluation(True, True, False)
print("(False and not true) or True : " + str(falseab) + " | Passed = " + str(falseab == False))

# Evaluate (True and not False) or 'Do Not Evaluate' (True)
ignorec = boolean_evaluation(True, False, 'Do Not Evaluate')
print("Evaluate (True and not False) or 'Do Not Evaluate': " + str(ignorec) + " | Passed = " + str(ignorec == True))

# Compare Seq [1, 'a', 3] == [1, 'a', 3] = 0
compseq0 = compare_sequences([1, 'a', 3], [1, 'a', 3])
print("is 1, a, 3 == 1, a, 3 == 0: " + str(compseq0) + " | Passed = " + str(compseq0 == 0))

# Compare Seq [1, 'a', 3] < [1, 'b', 3] = -1
compseq2 = compare_sequences([1, 'a', 3], [1, 'b', 3])
print("is 1, a, 3 < 1, b, 3 == -1: " + str(compseq2) + " | Passed = " + str(compseq2 == -1))

# Compare Seq [1, 'a', 4] > [1, 'a', 3] = 1
compseq1 = compare_sequences([1, 'a', 4], [1, 'a', 3])
print("is 1, a, 4 < 1, a, 3 == 1: " + str(compseq1) + " | Passed = " + str(compseq1 == 1))

print("\n*** END OF TEST ***\n")