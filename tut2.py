age = input("enter your age:")
age = int(age)
if(age>=1) and (age<=18 ):
    print("Important Birthday")
 
elif(age == 21) or (age ==50):
    print("Important too")

elif(not(age<65)):
    print("Not Important Birthday")
else:
    print("Sorry! Your Birthday is not imp")
