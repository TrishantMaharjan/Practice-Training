# num = float(input("Enter a number: "))
# check = num % 5
# if check == 0:
#     print("It is divisible.")
# else:
#     print("It is not divisible.")

num = float(input("Enter a number: "))
check1 = num % 3
check2 = num % 5
check3 = num % 7
if check1 == 0:
    print("{} is divisible by 3.".format(num))
elif check2 == 0:
    print("{} is divisible by {}.".format(num, 5))
elif check3 == 0:
    print("It is divisible by 7.")
else:
    print("It is not divisible by 3, 5 or 7.")
