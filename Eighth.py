# filter
# filter(function, iterable_object)

# alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# newlist = list(filter(lambda num: num % 2 != 0, alist))
# print(newlist)

# emails = ["1@gmail.com", "2@gmail.com",
#           "3@yahoo.com", "4@hotmail.com", "5@gmail.com"]
# newlist = list(filter(lambda email: email.endswith("@gmail.com"), emails))
# print(newlist)

# alist = [10, 20, 7, 9, "def", 8, "abc"]
# newlist = sum(filter(lambda number: isinstance(number, int), alist))
# print(newlist)

# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)


# num = int(input("Enter a number: "))
# print(factorial(num))

# def power(num, pow):
#     if pow == 0:
#         return 1
#     else:
#         return num * power(num, pow-1)


# base = int(input("Enter a number: "))
# p = int(input("Enter power: "))
# print(power(base, p))

# def power(num, pow):
#     if pow == 0:
#         return 1
#     else:
#         return num * power(num, pow-1)


# base = int(input("Enter a number: "))
# p = int(input("Enter power: "))
# print(power(base, p))


uname = "ram@gmail.com"
pword = "123@abcd"

username = "Dummy"
password = "Dummy"
while (username != uname or password != pword):
    username = input("Enter username: ")
    password = input("Enter password: ")
else:
    print("Login successful")

# else runs only when the loop is completely ran. It won't run if break is used.
