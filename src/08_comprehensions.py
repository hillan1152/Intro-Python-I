# """
# List comprehensions are one cool and unique feature of Python.
# They essentially act as a terse and concise way of initializing
# and populating a list given some expression that specifies how
# the list should be populated.

# Take a look at https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
# for more info regarding list comprehensions.
# """

# # Write a list comprehension to produce the array [1, 2, 3, 4, 5]

# y = [x + 1 for x in range(5)]
# print(y)

# # Write a list comprehension to produce the cubes of the numbers 0-9:
# # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]

# y = [x ** 3 for x in range(10)]

# print(y)

# # Write a list comprehension to produce the uppercase version of all the
# # elements in array a. Hint: "foo".upper() is "FOO".

# a = ["foo", "bar", "baz"]

# y = [letter.upper() for letter in a]

# print(y)

# # Use a list comprehension to create a list containing only the _even_ elements
# # the user entered into list x.

# x = input("Enter comma-separated numbers: ").split(",")

# # What do you need between the square brackets to make it work?
# # y = [int(num) for num in x if int(num) % 2 == 0]
# y = [i for i in x if int(i) % 2 == 0]
# print(y)

# List of Veggies
class Veggies:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __repr__(self):
        return "<Veggies: %s, %s>" % (self.name, self.color)


food = [
    Veggies("broccoli", "green"),
    Veggies("carrots", "orange"),
    Veggies("greenbeans", "light-green"),
    Veggies("okra", "brown"),
    Veggies("cabbage", "white"),
]
stew = [
    Veggies("somefood", "green"),
    Veggies("other food", "orange"),
    Veggies("this food", "light-green"),
    Veggies("that food", "brown"),
    Veggies("dis food", "white"),
]

theList = ["stern", "berg", "ran", "away", "from", "a", "balcony"]

# q = [f.color for f in food if f.color[1] == "r"]


def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        for q in arr:
            print(len(q))
            if len(q) == 5:
                return str(arr)
            else:
                return 0

    # print(len(arr[0]))
    #     if len(index) == 4:
    #         return order
    #     else:
    #         return "GAP"
    # return arr


selection_sort(theList)
