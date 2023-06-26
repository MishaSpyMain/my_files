def ext_func():
    """"hello we make our function"""
    my_var = 0
    def int_func():
        nonlocal my_var
        my_var +=1
        return my_var
    return int_func()
print()
"""this doesent matter, by this i mean this message. No one will ever see it."""