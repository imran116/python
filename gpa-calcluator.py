bangla = int(input("Enter marks for Bangla[1-100]:"))
english = int(input("Enter marks for English[1-100]:"))
math = int(input("Enter marks for Math[1-100]:"))
science = int(input("Enter marks for Science[1-100]:"))

avg = (bangla + english + math + science)/4

if(avg<0):
    print("Please Enter Valid Number!")
elif(avg>100):
    print("Your marks should not be over 100")
else:
    if(avg<=40):
        print("Your Avg number is :" + str(avg))
        print("Your Grade is F")
    elif(avg<=60):
        print("Your Avg number is :" + str(avg))
        print("Your Grade is D")
    elif(avg<=70):
        print("Your Avg number is :" + str(avg))
        print("Your Grade is C")
    elif(avg<=80):
        print("Your Avg number is :" + str(avg))
        print("Your Grade is B")
    elif(avg<=90):
        print("Your Avg number is :" + str(avg))
        print("Your Grade is A")
    else:
        print("Your Avg number is :" + str(avg))
        print("Your Grade is A+")
