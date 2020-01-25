age=input("Enter your age")
age=int(age)
if (age == 5):
    print("Go to the kindergarden")
standard = age-5
if (age>=6) and (age<=17):
    print("Your standard is {}".format(standard))
elif (age<17):
    print("You have to attend the college")

else:
    print(" Let's Nachooo")


