def say_hello(name, city, state):
    return("Hello, " + " ".join(name) +"!" + " Welcome to {}, {}!".format( city, state))


say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')
