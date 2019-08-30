# Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string. Go to the editor
# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# a modify_string
# enter ener
# two function ' -> slicing , the other slicing according the condition

def modify_string(p_string):
    #    len_of_str = len(p_string)
    # if len_of_str >= 2:
    #     return slice_string(p_string)
    # else:
    #     return '' conditional
    return slice_string(p_string) if len(p_string) >= 2 else ''


def slice_string(p_string):
    sliced_string = p_string[0:2] + p_string[-2:]
    return sliced_string


def test_str_longer_than_2_chars():
    assert modify_string('enter') == 'ener'


# print("hey"[-2:])

def test_str_equal_to_2_chars():
    assert modify_string('w3') == 'w3w3'


def test_str_len_less_than_2_chars():
    assert modify_string('w') == ''
