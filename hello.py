def greet(*names):
    print("Welcome " +names[1])

def mini_cal(num1, num2):
    return num1 + num2

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
print(mini_cal(num1, num2))