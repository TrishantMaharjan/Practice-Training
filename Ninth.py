# def outer_func():
#     def first_child():
#         print("I am 1st child")

#     def second_child():
#         print("I am 2nd child")

#     first_child()
#     second_child()


# outer_func()
# first_child() - this gives error as the scope of first_child is within outer_func only
# second_child() - this gives error as the scope of second_child is within outer_func only

# def calculator(operator):
#     def add(num1, num2):
#         return num1 + num2

#     def product(num1, num2):
#         return num1 * num2

#     if operator == "+":
#         return add
#     elif operator == "*":
#         return product


# a = calculator("+")
# res = a(10, 20) # a returns add, function is called outside the parent function
# print(res)

# decorator

# def greetings(func):
#     def wrapper():
#         print("Welcome to College")
#         func()
#         print("Welcome Again!")
#     return wrapper


# @greetings
# def hello():
#     print("Hello students!")


# hello()
# #greet = greetings(hello)
# # greet()
# # line 43, 48 works same as like 49 and 50

# def smart_division(func):
#     def wrapper(a, b):
#         if b == 0:
#             return "Can not divide by 0"
#         else:
#             return func(a, b)
#     return wrapper


# @smart_division
# def division(a, b):
#     return a/b


# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2nd number: "))
# print(division(num1, num2))
