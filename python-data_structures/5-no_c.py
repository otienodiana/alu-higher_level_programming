#!/usr/bin/python3
def no_c(my_string):
        if "c" and "C" in my_string:
            new_string = my_string.translate({ord("c"):None, ord("C"):None})
            return new_string
        else:
            return  c is not
