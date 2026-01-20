def my_function(*args, **kwargs):
    print(args)
    print(kwargs)


# my_function(1, 2, 3, x=1, h1=2, arg1=7, arg5=5, h=6)

import time
from datetime import datetime


def timer_function(arg):
    def return_function(*args, **kwargs):
        print("outer called")
        print(f"function started at {datetime.now()}")
        arg(*args, **kwargs)
        print(f"function ended at {datetime.now()}")

    return return_function


# @timer_function
# result = outer_function(standard_function) ; result()
def data_fetch_function(val, val2, val3):
    print("data fetc called")
    print(val)
    time.sleep(2)
    data_cleaning(val, val2, val3, 6, 78)


@timer_function
def data_cleaning(val, val4, val7, val9, val8):
    print("cleaning")
    time.sleep(1)


result = timer_function(data_fetch_function)
result()

# data_fetch_function(1, 2, 3)
