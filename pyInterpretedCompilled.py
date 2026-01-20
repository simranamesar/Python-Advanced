a = 1
# print(a)
# print("a")
# some_function()


import dis


def some_function():
    a = 1
    if a == 1:
        print("yes")


dis.dis(some_function)
