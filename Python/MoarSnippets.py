Red = str(input("Please enter your name: "))
age = int(input("How old are you, {0}?".format(Red)))
print(age)

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Come back when you are older!!")