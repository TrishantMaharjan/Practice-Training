# positional argument and keyword argument

# def profile(name, contact, address):
#     print(f"Name: {name}\nContact: {contact}")
#     print(f"Address: {address}")


# profile("Ram", "9876", "Kathmandu")
# print("-----------------------")
# profile(contact="987654", name="Shyam", address="Lalitpur")

# def example(*a):
#     print(f"Arguments: {a}")


# example(1, 2, 3, 4, 5)


# def example(*args):
#     print(f"Arguments: {args}")
#     for item in args:
#         print(f"Values: {item}")


# example(1, 2, 3, 4, 5)

# def example2(**kwargs):
#     print(f"Keyword Arguments: {kwargs}")


# example2(name="Ram", a=1, b=2)


# def example3(*args, **kwargs):
#     print(args, kwargs)


# example3(1, 2, 3, name="Ram", a=1, b=2)

# def square_root(num):
#     return num**0.5


# ans = square_root(100)
# print(f"Square root: {ans}")
# sq = square_root
# print(square_root)
# print(sq)
# ans2 = sq(144)
# print(f"Square root: {ans2}")

# def welcome(name):
#     print(f"Welcome {name}")


# def greet_ram(Var):
#     Var("Ram")


# greet_ram(welcome)

# def welcome(name):
#     return f"Welcome {name}!"


# def greet_ram(Var):
#     return Var("Ram")


# print(greet_ram(welcome))

# def total(num1, num2):
#     return num1 + num2


# def square_root(func, num1, num2):
#     return (func(num1, num2)**0.5)


# print(square_root(total, 10, 6))

# lambda function

# lambda par1, par2, ... : para1 + para2 + ...
# def a(a, b): return a+b


# print(a(5, 6))

# higher order function
# map(func, iterable_object)

# def increase_by_one(num):
#     return num+1


# alist = [2, 3, 4, 5, 6, 11, 14, 15]
# b1 = map(increase_by_one, alist)
# print(list(b1))

# b2 = map(lambda num: num+1, alist)
# print(list(b2))

namelist = [
    "ram", "shyam", "hari", "sita", "gita"
]
# newlist = ["Ram", "Shyam", "Hari", "Sita", "Gita"]

newlist = map(lambda newlist: newlist.capitalize(), namelist)
print(list(newlist))
print(list(map(str.capitalize, namelist)))
