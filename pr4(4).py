m=int(input("Enter your marks : "))
if (m>100 and m<0) : print("Invalid marks")
elif (m>=90 and m<=100) : print("Your grade is A")
elif (m>=80 and m<90) : print("Your grade is B")
elif (m>=70 and m<80) : print("Your grade is C")
elif (m>=60 and m<70) : print("Your grade is D")
elif (m>=50 and m<60) : print("Your grade is E")
elif (m>=0 and m<50) : print("Your grade is F")
else : print("Error")