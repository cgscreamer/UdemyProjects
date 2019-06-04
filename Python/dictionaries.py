fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

#To add to a dictionary
fruit["pear"] = "an odd shaped apple"

#To delete a dictionary entry
#del fruit["lime"]

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])

while True:
    dict_key = raw_input("Please enter a fruit: ")
    if dict_key == "quit":
        break
    description = fruit.get(dict_key, "We don't have a " + dict_key)
    print(description)


#To clear/empty the dictionary
#fruit.clear