def begin_generator(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        result.__next__()
        return result

    return inner_function


@begin_generator
def my_generator():
    print("generator called")
    input = yield
    print(input)
    print("yielded")
    input = yield 3
    print(input)
    print("complete")
    yield


result = my_generator()
# result.__next__()
result.send(100)
result.__next__()
# result.send(90)
# print("something in programmin")
# result.__next__()
# result.__next__()
