#Q1

name = input("Enter name: ")
print(name)

#Q2

firstName = input("Enter first name:")
surName = input("Enter surname: ")


#Q3

print("What do you call a bear with no teeth? \nA gummy bear!")

#Q4

firstNumber = int(input("Enter first number"))
secondNumber = int(input("Enter second number"))
total = firstNumber + secondNumber

print(total)

#Q5

firstNumber = int(input("Enter first number"))
secondNumber = int(input("Enter second number"))
thirdNumber = int(input("Enter third number"))

total = (firstNumber + secondNumber)* thirdNumber
print(total)

#Q6

startPizza = int(input("How many slices of the pizza have you started with?"))
slices = int(input("How many slices have you ate"))
total = startPizza - slices

print(f"You have {total} slices left")

#Q7

name = input("Enter name:")
age = (int(input("Enter age:")))
newAge = age + 1

print(f"{name} your next birthday you will be {newAge}")

#Q8

bill = int(input("What is the total"))
dinners = int(input("How many dinners are there"))
total = bill / dinners

print(total)

#Q9

days = int(input("Number of days"))
hours = days * 24
minutes = days * 1440
seconds = days * 86400

print(f"There are {hours} hours, {minutes}, minutes and {seconds} seconds in {days} days")

#Q10

kilograms = float(input("Enter kilograms: "))
pounds = kilograms * 2.204

print(pounds)

#Q11

bigNumber = int(input("Enter a number above 100"))
smallNumber = int(input("Enter a number below 10"))
total = bigNumber // smallNumber

print(f"{smallNumber} goes into {bigNumber} {total} times")

#Q12

firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

if firstNumber > secondNumber:
    print(firstNumber, secondNumber)
else:
    print(secondNumber,firstNumber)

#Q13

number = int(input("Enter a number that is under 20:"))

if number >= 20:
    print("Too high")
else:
    print("THank you")

#Q14

number = int(input("Enter number between 10 and 20:" ))

if number in range(10,20):
    print("Thank you")
else:
    print("Incorrect answer")

#Q15

colour = input("Input favourite colour: ")

if colour == "red" or "RED" or "Red":

    print("I like red too")

else:

    print(f"I don't like {colour}, I preffered")

#Q16

raining = input("Is it raining")
raining = raining.lower()

if raining == "yes":
   

    windy = input("Is it windy?")
    windy = windy.lower()

    if windy == "yes":
        print("It is too windy for an umbrella")

    else:
        print("Take an umbrella")

    

else:
    print("Enjoy your day")

#Q17

age = int(input("Enter age"))

if age == 18:
    print("You can drive")
elif age == 17:
    print("You can buy lottery ticket")
elif age < 18:
    print("You can go trick or treating")

#Q18

number = int(input("Enter a number"))

if number < 10:
    print("Too low")
elif number in range(10,20):
    print("Correct")
else:
    print("Too high")
