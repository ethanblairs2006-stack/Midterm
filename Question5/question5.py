# lists are mutable - you can change an element directly
my_list = ["a", "b", "c"]
my_list[0] = "z"
print(my_list)  # ['z', 'b', 'c'] - the original list was modified

# strings are immutable - trying to change a character raises a TypeError
my_string = "abc"
# my_string[0] = "z"  # this would crash: TypeError: 'str' object does not support item assignment

# to get a modified string, you have to build a brand new one
my_string = "z" + my_string[1:]
print(my_string)  # 'zbc' - but this is a new string, not the original changed
