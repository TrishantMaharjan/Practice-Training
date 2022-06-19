# def addition(a, b):
#     return a + b

# print(addition('1', '2'))

# def welcome():
#     print("Welcome Students")


# # welcome => call by reference.
# welcome()
# # Function signature, function executes only when we call it's signature.
# print(type(welcome))


def hello(college_name):
    name = "Students"
    print(f"Welcome {name} of {college_name}!")


college_name = ["KEC", "IOE", "Advanced", "Khwopa"]
i = 0

for item in college_name:
    hello(college_name[i])
    i = i+1
