import math
# Python datatypes - String

# mystring1 = "kumar"
# mystring2 = 'kumar'
# print(type(mystring2))
#
# # Exercise 1
# # Print the initials
# firstName = input("Enter your firstname: ")
# middleName = input("Enter your middle name: ")
# lastName = input("Enter your last name: ")
# print("Your initials are " + firstName[0] + middleName[0] + lastName[0])

# Exercise 2
# Print the product information
# productId = "037-00901-00027"
# print("Country code:" + productId[:3])
# print("Product code:" + productId[4:9])
# print("Batch number:" + productId[10:])

# Exercise 3
# Calculate the area and circumference of a circle
user_radius = float(input("Enter the radius of the circle: "))
print("The area =", (math.pi * math.sqrt(user_radius)))
print("The circumference =", (2 * math.pi * user_radius))
