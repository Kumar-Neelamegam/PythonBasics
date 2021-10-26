import random

# ---------------------------------
# if statement and elsif
# and or

# BMI calculation Exercise 1
# personWeight = float(input("Enter your body weight in (Kg):"))
# personHeight = float(input("Enter your body height in (Meters):"))
#
# bmiCalculated = float(personWeight / (personHeight * personHeight))
#
# if bmiCalculated <= 18.5:
#     print("You are underweight")
# elif 18.5 < bmiCalculated <= 24.9:
#     print("You are normal weight")
# elif 24.9 < bmiCalculated <= 29.9:
#     print("You are overweight")
# elif bmiCalculated >= 30:
#     print("You are obesity")
# ---------------------------------
# while loop
# people = []
# while len(people) < 5:
#     person = input("Enter the name of a person:")
#     people.append(person)
# print(people)
# ---------------------------------
# random number guess
# number = random.randint(0, 10)
# guess = int(input("Enter the number to guess:"))
# while True:
#     if guess == number:
#         break
#     else:
#         guess = int(input("No try again:"))
# print("You guessed it", number)
# ---------------------------------
# For loop
# name = "Muthukumar Neelamegam"
# for i in name:
#     print(i)
#
# bioData = {"Name": "Kumar", "Age": 30, "Address": "Linz, Austria"}
# for x in bioData:
#     print(x, ":", bioData[x])
#
# arrayList = {"Number": [1, 2, 3, 4, 5], "Alphabets": ["A", "B", "C", "D", "E"]}
# for listItem in arrayList:
#     print("Keys:", listItem)
#     for item in arrayList[listItem]:
#         print("Values:", item)

# Loops Exercise 1
# x = 0
# peopleList = []
# while x <= 8:
#     if x == 8:
#         print("You selected:", peopleList[1])
#         break
#     peopleList.append(input("Enter the person name:"))
#     x += 1

colours = ["red", "orange", "blue", "white", "black"]

while True:
    color = colours[random.randint(0, len(colours)-1)]
    selectedColor = input("Guess the color:")

    while True:
        if color == selectedColor.lower():
            break
        else:
            selectedColor = str(input("No try again: "))

    print("You guessed the color:", selectedColor.lower())
