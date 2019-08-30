# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'
# a='abc'
# b='xyz'
# b[0:upto 1- length]+a[length-]1]

def str_manipulator(p_string,q_string):
    part_one= q_string[0:-1]+ p_string[-1]
    part_two= p_string[0:-1]+ q_string[-1]
    return part_one + " " + part_two

def test_swap_case():
    assert str_manipulator('abc','xyz') == 'xyc abz'