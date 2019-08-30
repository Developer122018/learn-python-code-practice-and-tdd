# Write a Python program to count the number of characters (character frequency) in a string.

# goggle : {'g':1,'o':2,'l':1,'e':1}
# input --
# return_frequency(String argument) return will be dictionary
# algo
# empty dictionary ={}
# loop over string
# list of the keys -> []
# iterate over the []

def return_frequency(p_string):
    str_dict = {}
    for i in p_string:
        key = str_dict.keys()  # []
        if i in key:
            str_dict[i] += 1
        else:
            str_dict[i] = 1
    return str_dict


my_dict = return_frequency(input('what is your string?'))
print(my_dict)