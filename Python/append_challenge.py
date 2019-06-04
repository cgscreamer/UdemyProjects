with open("NewText.txt", "w") as Table:
    for num in range (11):
        out = num * 2
        Table.write("{} times 2 is {} \n".format(num, out))