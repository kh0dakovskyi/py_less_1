# class Dog:
#     def data(self, name, sex):
#         self.age = 7
#         print(name, "Gav", self.age, sex)
#
#
# dog1 = Dog()
# dog1.data("maksim", "trans")
# dog2 = Dog()
# dog2.data("archi", "devka")


class Dog:
    def __init__(self, name, sex):
        self.age = 7
        print(name, "Gav", self.age, sex)


dog1 = Dog("Pika", "male")
dog2 = Dog("Nester", "female")






# def data(name, age=6):
#     print(name, "Gav", age)

# a = data("pedic")