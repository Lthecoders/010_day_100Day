# ----------day 10 challenge---------

print("tip calculator")
print("--------------\n")

myBill = float(input("What was the bill?: "))
tipPercentage = int(
    input("What percentage of tip would you like to add (15, 18, 20)?: "))
numberOfPeople = int(input("How many people?: "))

tipAmount = myBill * (tipPercentage / 100)
totalBill = myBill + tipAmount
answer = totalBill / numberOfPeople

print(f"The total bill amount including tip is: {round(totalBill)} $")
print(f"Each person needs to pay: {answer} $")
