# take input(int.) from a user
# cheack if u input is int else break
# check if input is divisible by 5
# if true print input number is divisible by 5 and leaves 0 as reminder
# else print number is not divisible by 5 and leaves (..) as reminder

num = float(input("Enter a digit: "))

if num % 5 == 0:
    print(num, ' is divisible by 5 and leaves 0 as reminder')

elif num % 5 != 0:
    print(num, ' is not 46divisible by 5 and leaves ', num%5, 'as reminder')

else:
    print("I don't quite get you.")