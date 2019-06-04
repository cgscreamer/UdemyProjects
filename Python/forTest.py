number = "9,234,567,789,567"
cleanedNumber = ""

for char in number:
    if char in "0123456789":
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)

print("The number is {}".format(newNumber))