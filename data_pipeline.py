def begin_coroutine(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        result.__next__()
        return result

    return inner_function


def data_pipeline_start(file, next_stage):
    while True:
        line = file.readline()
        if not line:
            break
        next_stage.send(line)


@begin_coroutine
def filter_word(keyword, next_stage):
    while True:
        line = yield
        if keyword in line:
            next_stage.send(line)


@begin_coroutine
def db_insert():
    while True:
        line = yield
        print(f"insert {line} in db")


file = open(
    "/Users/D068192/dev/codes/git/srh/bdp-oct25-classroom-bdp_oct25_all/codes/bible.txt"
)

data_pipeline_start(file, filter_word("God", db_insert()))
