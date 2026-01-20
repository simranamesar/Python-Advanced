def my_function(val):
    # print("hi")
    print(val)
    return "abc"


b = "srh"
a = my_function(b)
# print(a)

z = my_function
z(1)
# data type should be assingable to variable


# data type should be passable into a function
#


def outer_function(val):
    val()

    def inner_function():
        print("inner")

    return inner_function


def my_function():
    print("my_function")


t = my_function

j = outer_function(t())
