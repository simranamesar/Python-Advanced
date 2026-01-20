# from utilities.database import insert
import sys

import pandas

print(sys.path)


class StackOverflow:
    noOfActiveUsers = 30

    def __init__(self, id, name, active, numberOfQuestionsAsked=None):
        print("called")
        self.id = id
        self.name = name
        self.active = active
        self.numberOfQuestionsAsked = numberOfQuestionsAsked

    def change_active(self, newValue):
        # type check
        self.active = newValue

    @classmethod
    def change_active_user(cls, newValue):
        cls.noActiveUsers = newValue


user1 = StackOverflow(1, "anil", True, 100)
print(user1.active)

user1.change_active(False)
user2 = StackOverflow(2, "someone", False)
print(user1.active)
# user1.numberOfQuestionsAsked = 100
print(user1.numberOfQuestionsAsked)
print(user2.numberOfQuestionsAsked)


StackOverflow.change_active_user(300)
print(StackOverflow.noActiveUsers)

# print(dir(user1))
# print(type(user1))
a = "anil"
# print(type(1))
# print(dir(a))


def some_function():
    None


a = [1, 2, 3]
print(a)
# b = [x for x in range(,1000000)]
# print(b)
print(vars(user1))

df = pandas.DataFrame(vars(x) for x in [user1, user2])
print(df)
print(df.describe())
# print(type(some_function))
