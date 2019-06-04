#test = open("C:\Users\ccreamer\Documents\UdemyProjects\Python\Test.txt", 'r')

with open("Test.txt", 'r') as testing:
    lines = testing.readlines()
for line in lines:
    print(line)

