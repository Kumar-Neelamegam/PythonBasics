# Data types: Lists and Tuples
# Lists
studentsList = ["Muthu", "Kumar", "Prem"]
print(len(studentsList))

print(studentsList[0])
print(studentsList[-1])
studentsList.append("Neelamegam")
print(studentsList)
studentsList.remove("Kumar")
studentsList.pop(1)
studentsList.insert(-1, "Jegadheswari")
print(studentsList)

# Tuples
months = {"Jan", "Feb", "Mar"}
print(type(months))

# Exercise 2
# peopleList = ["A", "B", "C"]
# print(peopleList)
#
# peopleList.append(input("Enter the person name:"))
# print(peopleList)

# ===================================
# Dictionaries
# Exercise 1
# months1 = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Apr", "05": "May", "06": "Jun", "07": "Jul", "08": "Aug",
#            "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}
# dateofbirth = input("Enter your date of birth in this format (DD-MM-YYYY):")
# print("You were born in ", months1[dateofbirth[3:5]])

person = {"name": "kumar"}
person["childrens"] = ["A", "B", "C"]
print(person)
person["childrens"].append("D")
print(person)

# Exercise
personDictionary = {"name": "kumar", "gender": "male", "age": "30", "address": "Austria, Linz", "phone": "+4368864865193"}
print(personDictionary)
dataKey = input("What information do you want to know? ")
print(personDictionary.get(dataKey, "No data found"))

