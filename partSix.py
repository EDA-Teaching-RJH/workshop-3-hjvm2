age = int(input("What's your age? "))
stu = input("Are you a student? ").lower() 

if age <= 12 or age >= 65:
    print("Ticket cost: £5")

elif age > 12 and age < 65 and stu == 'no':
    print("Ticket cost: £10")

elif age > 12 and age < 65 and stu == 'yes':
    print("Ticket cost: £8")

else:
    print("N/a")