import unittest
from functions import (
    create_tuple,
    unpack_tuple,
    tuple_details,
    create_set,
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

class TestFunctions(unittest.TestCase):

    # --- Tuples and Sequences Tests ---
    def test_create_tuple(self):
        self.assertEqual(create_tuple(1, 2, 3, 'a'), (1, 2, 3, 'a'))
    
    def test_unpack_tuple(self):
        self.assertEqual(unpack_tuple((1, 2, 3)), [1, 2, 3])
    
    def test_tuple_details_non_empty(self):
        details = tuple_details((1, 2, 3))
        expected = {'length': 3, 'first': 1, 'last': 3}
        self.assertEqual(details, expected)
    
    def test_tuple_details_empty(self):
        details = tuple_details(())
        expected = {'length': 0, 'first': None, 'last': None}
        self.assertEqual(details, expected)
    
    # --- Set Operations Tests ---
    def test_create_set(self):
        self.assertEqual(create_set([1, 2, 2, 3]), {1, 2, 3})
    
    def test_unique_sorted(self):
        self.assertEqual(unique_sorted([3, 1, 2, 3, 4, 1]), [1, 2, 3, 4])
    
    # --- Dictionary Operations Tests ---
    def test_create_dictionary(self):
        self.assertEqual(create_dictionary([('a', 1), ('b', 2)]), {'a': 1, 'b': 2})
    
    def test_update_dictionary(self):
        d = {'a': 1, 'b': 2}
        updated = update_dictionary(d, 'a', 10)
        self.assertEqual(updated, {'a': 10, 'b': 2})
    
    def test_delete_key_success(self):
        d = {'a': 1, 'b': 2}
        result = delete_key(d, 'a')
        self.assertEqual(result, {'b': 2})
    
    def test_delete_key_failure(self):
        d = {'a': 1, 'b': 2}
        with self.assertRaises(KeyError):
            delete_key(d, 'x')
    
    def test_dict_comprehension_example(self):
        # For numbers, value squared; for strings, length.
        result = dict_comprehension_example([2, "hello", 3])
        expected = {2: 4, "hello": 5, 3: 9}
        self.assertEqual(result, expected)
    
    # --- Looping Techniques Tests ---
    def test_iterate_dictionary(self):
        d = {"x": 100, "y": 200}
        result = iterate_dictionary(d)
        expected = ["x: 100", "y: 200"]
        # Since dictionary order is preserved (Python 3.7+), we check equality.
        self.assertEqual(result, expected)
    
    def test_enumerate_list(self):
        self.assertEqual(enumerate_list(['apple', 'banana']), [(0, 'apple'), (1, 'banana')])
    
    def test_zip_lists(self):
        self.assertEqual(zip_lists([1, 2], ['a', 'b']), [(1, 'a'), (2, 'b')])
    
    def test_reverse_and_sort(self):
        reversed_list, sorted_list = reverse_and_sort([3, 1, 2])
        self.assertEqual(reversed_list, [2, 1, 3])
        self.assertEqual(sorted_list, [1, 2, 3])
    
    # --- Conditions and Comparisons Tests ---
    def test_check_membership_true(self):
        self.assertTrue(check_membership([1, 2, 3], 2))
    
    def test_check_membership_false(self):
        self.assertFalse(check_membership("hello", "z"))
    
    def test_chained_comparison_true(self):
        self.assertTrue(chained_comparison(1, 2, 2))
    
    def test_chained_comparison_false(self):
        self.assertFalse(chained_comparison(2, 2, 3))
    
    def test_boolean_evaluation_true(self):
        self.assertEqual(boolean_evaluation(True, False, "fallback"), True)
    
    def test_boolean_evaluation_fallback(self):
        self.assertEqual(boolean_evaluation(False, True, "fallback"), "fallback")
    
    def test_compare_sequences_less(self):
        self.assertEqual(compare_sequences([1, 2, 3], [1, 2, 4]), -1)
    
    def test_compare_sequences_equal(self):
        self.assertEqual(compare_sequences("abc", "abc"), 0)
    
    def test_compare_sequences_greater(self):
        self.assertEqual(compare_sequences((3, 4), (1, 2)), 1)

if __name__ == "__main__":
    unittest.main()
