#Michelle Yick
#10-10-2014
#Character encoding HW (Theory)

answer = int(input("Would you like to convert 1.Binary to it's equivalent character or 2.Character to binary:"))

if answer == 1:
    binary = int(input("Please enter a 7 bit binary number"))
    if binary > 1111111 and binary < 0000000 or binary == 0000000:
        print("You have entered a number out of the range. Please enter a 7 bit binary number.")
    else:
        
