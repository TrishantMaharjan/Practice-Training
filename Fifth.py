# break continue

# for i in range(1, 5):
#     if i % 3 == 0:
#         print(f"Statement broke at i={i}")
#         break
#     print(i)

# for i in range(1, 5):
#     if i % 3 == 0:
#         print(f"Statement continued at i={i}")
#         continue
#     print(i)

# i = 1
# while i % 3 != 0:
#     print(i)
#     i = i + 1

# list comphrension

# lis = []
# for u in range(1, 40, 2):
#     lis.append(u)
# print(lis)

# lis = [i for i in range(1,51)]
# print(lis)

# oddlist = [item for item in range(1, 40, 2)]
# print(oddlist)

# evenlist = [item for item in range(0, 41, 2)]
# print(evenlist)

# alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evenlist = [i for i in alist if i % 2 == 0]
# print(evenlist)

# sum = 0
# for i in range(1, 51):
#     sum = sum + i

# print(sum)

# alist = [item for item in range(1, 51)]
# print(sum(alist))
# print(sum(range(1, 51)))

# user input 10 times, int
# evenlist, oddlist, duplicatelist, mainlist

# mainlist = []
# evenlist = []
# oddlist = []
# duplicatelist = []
# for i in range(1, 11):
#     num = int(input("Enter a number: "))
#     if num not in mainlist:
#         if num % 2 == 0:
#             evenlist.append(num)
#         else:
#             oddlist.append(num)
#     else:
#         duplicatelist.append(num)
#     mainlist.append(num)
# print(f"Main list {mainlist}")
# print(f"Odd list {oddlist}")
# print(f"Even list {evenlist}")
# print(f"Duplicate list {duplicatelist}")

Var1 = {"properties":
        {
            "profile":
            {
                "name": "Ram",
                "contact": ["9856732523", "8326623"],
                "address": ["Lalitput", "Kathmandu"],
            },
                "task":
                    [
                        {"category1": "Plumbing"},
                        {"category2": "Computer Technician"},
            ],
        },
        }

print("####### Profile ######")
print(f"Name: {Var1.get('properties', {}).get('profile', {}).get('name', {})}")
contacts = Var1.get('properties', {}).get('profile', {}).get('contact', {})
for idx, contacts in enumerate(contacts, 1):
    print(f"Contact {idx}: {contacts}")
adrs = Var1.get('properties', {}).get('profile', {}).get('address', {})
for idx, address in enumerate(adrs, 1):
    print(f"Address {idx}: {address}")
tasks = Var1.get('properties', {}).get('task', {})
for idx, task in enumerate(tasks, 1):
    print(f"Task {idx}: {task.get(f'category{idx}')}")

# for idx, item in enumerate(tasks, 1):
#     print(idx)
#     print(item.get(f'category{idx}'))

###### Profile ######
# Name: ___
# Contact: _______
# Address: ______
# Task: ______
