# We know that to get the Young's Modulus, we divide stress by strain,
# This is a quick programme to do that for us -especially in cases where
# we're dealing with varying numbers.

stress = raw_input("What is the stress (in newtons)?: ")
strain = raw_input("What is the strain (in milimetres)?: ")


if stress == "":
    Youngs_Modulus = raw_input("What is the Young's Modulus?: ")
    Answer_2 = float(Youngs_Modulus)/float(strain)
    print("The stress is " + str(Answer_2))
elif strain == "":
    Youngs_Modulus = raw_input("What is the Young's Modulus?: ")
    Answer_3 = float(Youngs_Modulus) * float(stress)
    print("The strain is" + str(Answer_3))
else:
    Answer_1 = float(stress)/float(strain)
    print("The Young's Modulus is " + str(Answer_1))
