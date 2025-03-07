Laboratory 4<br>
Advanced Data Structures, Looping Techniques, and Enhanced Dictionary Operations in Python<br>
Objective:<br>
Create a Python program to practice and demonstrate the following concepts:<br>
•	Tuples and Sequences: Packing/unpacking tuples, handling empty tuples and one-item tuples.<br>
•	Sets: Creating sets, performing membership tests, executing set operations (union, intersection, difference, and symmetric difference), and using set comprehensions.<br>
•	Dictionaries: Creating, updating, and merging dictionaries, using dictionary comprehensions, and applying dictionary methods.<br>
•	Looping Techniques: Iterating over dictionaries with .items(), lists with enumerate(), pairing sequences with zip(), and looping in reverse or sorted order.<br>
•	Conditions and Comparisons: Using membership operators, chained comparisons, Boolean logic (including short-circuit evaluation), and lexicographical ordering.<br>
•	Additional Challenges: Merging multiple dictionaries and checking if a sequence is strictly increasing.<br>
________________________________________
Assignment Tasks
1. Create functions.py<br>
At the top of the file, include your name, date, and a brief description of the file’s purpose as comments.<br>
Implement the following functions. For each function, include:<br>
•	Function name:<br>
•	Description:<br>
•	Arguments:<br>
•	Return:<br>
Make sure that the Arguments and Return sections are formatted so that the description for each item lines up correctly.<br>
________________________________________
A. Tuples and Sequences<br>
1.	Function name: create_tuple<br>
Description:<br>
Pack the provided arguments into a tuple and return it.<br>
Arguments:<br>
*args : A variable number of arguments to be packed into a tuple.<br>
Return:<br>
A tuple containing all the provided arguments.<br>
2.	Function name: unpack_tuple<br>
Description:<br>
Unpack the tuple into individual variables and return them as a list.<br>
(Assume the tuple has a fixed, known number of elements.)<br>
Arguments:<br>
t : A tuple to be unpacked.<br>
Return:<br>
A list of the unpacked elements.<br>
3.	Function name: tuple_details<br>
Description:<br>
Return a dictionary containing details about the tuple such as its length, the first element, and the last element.<br>
Handle the case of an empty tuple appropriately.<br>
Arguments:<br>
t : A tuple whose details are to be extracted.<br>
Return:<br>
A dictionary with keys such as 'length', 'first', and 'last'.<br>
________________________________________
B. Set Operations<br>
4.	Function name: create_set<br>
Description:<br>
Create a set from the given iterable.<br>
Arguments:<br>
iterable : An iterable from which to create a set.<br>
Return:<br>
A set containing unique elements from the iterable.<br>
5.	Function name: set_operations<br>
Description:<br>
Given two sets, perform various set operations and return the results in a dictionary.<br>
Arguments:<br>
s1 : The first set.<br>
s2 : The second set.<br>
Return:<br>
A dictionary with the following keys:<br>
- 'union' : The union of s1 and s2.<br>
- 'intersection' : The intersection of s1 and s2.<br>
- 'difference' : The difference (elements in s1 but not in s2).<br>
- 'symmetric_difference': The symmetric difference of s1 and s2.<br>
6.	Function name: unique_sorted<br>
Description:<br>
Return a sorted list of unique elements from the provided iterable.<br>
Arguments:<br>
iterable : An iterable that may contain duplicate elements.<br>
Return:<br>
A sorted list of the unique elements.<br>
________________________________________
C. Dictionary Operations<br>
7.	Function name: create_dictionary<br>
Description:<br>
Create a dictionary from a list of key-value pair tuples.<br>
Arguments:<br>
pairs : A list of tuples, where each tuple is a key-value pair.<br>
Return:<br>
A dictionary constructed from the provided pairs.<br>
8.	Function name: update_dictionary<br>
Description:<br>
Update the dictionary with the provided key-value pair.<br>
If the key exists, its value is overwritten.<br>
Arguments:<br>
d : The dictionary to update.<br>
key : The key to update or add.<br>
value : The value associated with the key.<br>
Return:<br>
The updated dictionary.<br>
9.	Function name: delete_key<br>
Description:<br>
Remove the specified key from the dictionary.<br>
If the key does not exist, return an error message or raise an exception.<br>
Arguments:<br>
d : The dictionary from which to delete a key.<br>
key : The key to be removed.<br>
Return:<br>
The dictionary after removal of the key, or an error message if the key is not found.<br>
10.	Function name: dict_comprehension_example<br>
Description:<br>
Create a dictionary using comprehension that maps each element of the iterable<br>
to its square (if numeric) or its length (if a string).<br>
Arguments:<br>
iterable : An iterable containing numbers and/or strings.<br>
Return:<br>
A dictionary with each element as a key and its corresponding computed value.<br>
11.	Function name: merge_dictionaries<br>
Description:<br>
Merge a list of dictionaries into a single dictionary.<br>
If the same key appears in multiple dictionaries, combine their values into a list.<br>
Arguments:<br>
dicts : A list of dictionaries to merge.<br>
Return:<br>
A dictionary where each key maps to a list of all values associated with that key from the input dictionaries.<br>
________________________________________
D. Looping Techniques<br>
12.	Function name: iterate_dictionary<br>
Description:<br>
Iterate over the dictionary and return a list of formatted strings showing key-value pairs.<br>
Arguments:<br>
d : The dictionary to iterate over.<br>
Return:<br>
A list of strings in the format "key: value".<br>
13.	Function name: enumerate_list<br>
Description:<br>
Enumerate over the list and return a list of tuples containing the index and the corresponding element.<br>
Arguments:<br>
lst : The list to enumerate.<br>
Return:<br>
A list of tuples where each tuple is (index, element).<br>
14.	Function name: zip_lists<br>
Description:<br>
Pair elements from two lists using the zip function and return the resulting list of tuples.<br>
Arguments:<br>
lst1 : The first list.<br>
lst2 : The second list.<br>
Return:<br>
A list of tuples, each containing one element from lst1 and the corresponding element from lst2.<br>
15.	Function name: reverse_and_sort<br>
Description:<br>
Return both a reversed version of the list and a sorted version of the list.<br>
Arguments:<br>
lst : The list to be processed.<br>
Return:<br>
A tuple with two lists:<br>
- The first is the reversed list.<br>
- The second is the sorted list.<br>
________________________________________
E. Conditions and Sequence Comparisons<br>
16.	Function name: check_membership<br>
Description:<br>
Check if a value exists within a sequence.<br>
Arguments:<br>
sequence : The sequence to search.<br>
value : The value to check for.<br>
Return:<br>
True if the value is found, otherwise False.<br>
17.	Function name: chained_comparison<br>
Description:<br>
Evaluate the chained comparison a < b == c and return the result.<br>
Arguments:<br>
a : The first value.<br>
b : The second value.<br>
c : The third value.<br>
Return:<br>
True if the comparison holds; otherwise, False.<br>
18.	Function name: boolean_evaluation<br>
Description:<br>
Evaluate the Boolean expression (a and not b) or c using short-circuit evaluation.<br>
Arguments:<br>
a : A Boolean or value evaluated in a Boolean context.<br>
b : A Boolean or value evaluated in a Boolean context.<br>
c : A Boolean or value evaluated in a Boolean context.<br>
Return:<br>
The result of the Boolean expression.<br>
19.	Function name: compare_sequences<br>
Description:<br>
Compare two sequences lexicographically.<br>
Arguments:<br>
seq1 : The first sequence.<br>
seq2 : The second sequence.<br>
Return:<br>
-1 if seq1 is less than seq2;<br>
0 if they are equal;<br>
1 if seq1 is greater than seq2.<br>
20.	Function name: is_strictly_increasing<br>
Description:<br>
Check if a sequence of numbers is strictly increasing<br>
(i.e., each element is less than the next one).<br>
Arguments:<br>
sequence : A list or tuple of numbers.<br>
Return:<br>
True if the sequence is strictly increasing, otherwise False.<br>
2. Create main.py (Driver Program)<br>
At the top of the file, include your name, date, and a brief description of the file’s purpose as comments.<br>
In main.py:<br>
•	Import Functions:<br>
Import all functions from functions.py.<br>
•	Testing Your Functions:<br>
For each function, write sample test cases that display the function’s input and output.<br>
Use inline comments to explain the test case and the expected result.<br>
•	Execution Block:<br>
Use the following block to ensure tests run only when the module is executed directly:<br>
## Submission<br>
Submit a zip file containing all the code files on Canvas.<br>
Naming Convention: `CWID_LastName_Firstname.zip`<br>
Your zipped folder should contain the following files:<br>
```
                  | > functions.py
                  | > main.py
                  | > test.py
                  | > test.sh (for UNIX-based systems)
                  | > win_test.bat (for Windows systems)
```
    
## Grading
1. All points add up to a total of 100 points possible as detailed below. Partial credit will be given where applicable.

| Points | Description |
| --- | --- |
|50|Environment setup and Lab Submission|
|20|All required files are submitted|
|30|All unit tests passed|
