#Michelle Yick
#03-10-2014
#Theory
#Character Encoding class exercise

print("You can convert: 1.number to character and 2.character to number")

answer = int(input("What do you want to do?"))


if answer ==1:
    number = int(input("What value would you like to convert?"))
    result = chr(number)
    print("The answer is {0}.".format(result))
    
elif answer ==2:
    character = input("What character would you like to convert?")
    result1 = ord(character)
    print("The answer is {0}.".format(result1))
