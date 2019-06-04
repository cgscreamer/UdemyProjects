import end as end

name = raw_input("Hey, what's your name? ")
age = input("And what age are you?")

print(name + " " + str(age))

number = "9,234,666.888.88.97.,88,8,8"

cleanerNumber = ''

for i in range(0, len(number)):
    if number[i] in "0123456789":
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print ("The number is {}".format(newNumber))