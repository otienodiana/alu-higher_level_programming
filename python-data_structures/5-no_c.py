#!/usr/bin/python3
def no_c(my_string):
        if "c" and "C" in my_string:
            new_string = my_string.translate({ord("c"):None, ord("C"):None})
            print(new_string)
        else:
            print("c is is not")
