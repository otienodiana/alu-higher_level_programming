#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord("c"):None, ord("C"):None})
    return new_string
print(no_c("Best School"))
print(no_c("Chicago")) 
print(no_c("C is fun!"))
