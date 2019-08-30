# # printing
# # global vat=riade fbles
# def append_one( list_var):
#     return list_var[-1:]
# #indexing starts from 0 at the start but from -1 from the end
# list1=[3,6,9]
# print(append_one(list1))
a=[1,2,3]
def appending(a):
    copy=a
    copy.append(5)
    return copy
print(appending(a))
print(a)
#dont return functions, return proper variables that have already been modified
#dont update global variables
# memory ram ->  locker name of the locker is a, inside the locker=[1,2,3]
# copy=a ,  copy=[1,2,3] copy=location of the locker a
# copy.append,  append at the location of copy=a ,  [1,2,3,5]
#copy = a. they both have the same memory location


