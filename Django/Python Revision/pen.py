# LINES = 3
# MIN_BET = 1
# MAX_BET = 100

# def deposit():
#     while True:
#         amount = input("Enter your amount:\n$ ")
#         if(amount.isdigit()):
#             amount = float(amount)
#             if(amount > 0):
#                 break
#             else:
#                 input("Amount must be greater than zero")

#         else:
#             input("Amount must a number")
    
#     return amount


# def amount_of_lines():
#     while True:
#         lines = input("Enter the number of lines:(1 - "+ str(LINES) +  ")? ")
#         if(lines.isdigit()):
#             lines = int(lines)
#             if(1 <= lines <= LINES):
#                 break
#             else:
#                 input("Enter a valid number of lines")

#         else:
#             input("Lines must a number")

#     return lines
    
# def get_bet():
#     while True:
#         amount = input("Enter the amount you are beting? ")

#         if amount.isdigit():
#             amount = int(amount)
#             if MIN_BET <= amount <= MAX_BET:
#                 break 
#             else:
#                 input("Amount must be just right")


#         else:
#             input("Amount must a number")

#     return amount




# def main():
#     balance = deposit()
#     lines = amount_of_lines()
#     while True:
#         bet = get_bet()
#         total_bet = (bet * lines)
#         if total_bet > balance:
#             print("Not enough money to be betting? Your current balance is $", balance)
            
#         else:
#             break

#     update = balance + total_bet
#     print(f"You are betting ${bet} on {lines}.\nYour update balance is ${update}")
#     print(f"\nThank you for your servics😍😍")
    

   

# main()








# def main():

#     while True:
  
#         try:
#             a = int(input("enter a first number: \n$ "))
#             b = int(input("enter a scond number: \n$ "))

#         except:
#             print("Enter a valid number")
#             continue

#         c = input("Enter the sign:\n1. +\n2. -\n3. x\n4. /\n5. Quit\n\n$ ")

#         if c == "5" or c.lower() == "quit" :
#             print("Exiting")
#             break
            
            

#         if c == "+" or c == "1":
#             add(a, b)
        
#         elif c == "-" or c == "2":
#             subtract(a, b)

#         elif c == "x" or c == "*" or c == "3":
#             multiply(a, b)

#         elif c == "/" or c == "4":
#             divide(a, b)

#         else: 
#             print("Enter the sign")
        
           

# def add(a, b):
#     print(a + b)

# def subtract(a, b):
#     print(a - b)

# def multiply(a, b):
#     print(a * b)


# def divide(a, b):
#     if b == 0:
#         print("imposible to divide a number by 0")
#     else:
#         print(a / b)

        
# main()












# """
# Create a mini quiz qame about country and their capital city
# it should have a question and 4 option the user must pick a option and if correct get 25 points if not 0
# """



# def que1(grade):
    
#     ans = input("What is the capital city of Ghana:\nA. Lagos\nB. Accra\nC. Maila\nD. Tokyo\n$ Answer: ")

#     if(ans.upper() == "A" or ans.upper() == "C" or ans.upper() == "D"):
        
#         print(f"WRONG!!❌❌")

#     elif(ans.upper() == "B"):
        
#         print(f"CORRECT!!!⭕⭕")
#         grade =+ 25

#     else:
#         print("Wrong input")


#     return grade



# def que2(grade):

#     ans = input("What is the capital city of Nigeria:\nA. Maila\nB. Lagos\nC. Accra\nD. Tokyo\n$ Answer: ")

#     if(ans.upper() == "A" or ans.upper() == "C" or ans.upper() == "D"):
        
#         print(f"WRONG!!❌❌")

#     elif(ans.upper() == "B"):

        
#         print(f"CORRECT!!!⭕⭕")
#         grade =+ 25

#     else:
#         print("Wrong input")

#     return grade

# def que3(grade):
#     ans = input("What is the capital city of Japan:\nA. Warsaw\nB. Abuja\nC. Accra\nD. Tokyo\n$ Answer: ")

#     if(ans.upper() == "A" or ans.upper() == "C" or ans.upper() == "B"):
        
#         print(f"WRONG!!❌❌")

#     elif(ans.upper() == "D"):

       
#         print(f"CORRECT!!!⭕⭕")
#         grade =+ 25

#     else:
#         print("Wrong input")

#     return grade


# def que4(grade):
#     ans = input("What is the capital city of Poland:\nA. Rome\nB. Abuja\nC. Warsaw\nD. Tokyo\n$ Answer: ")

#     if(ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "D"):
        
#         print(f"WRONG!!❌❌")

#     elif(ans.upper() == "C"):

        
#         print(f"CORRECT!!!⭕⭕")
#         grade =+ 25

#     else:
#         print("Wrong input")
    
#     return grade


# def que5(grade):
#     ans = input("What is the capital city of Italy:\nA. Rome\nB. Abuja\nC. Warsaw\nD. Tokyo\n$ Answer: ")

#     if(ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "D"):
        
#         print(f"WRONG!!❌❌")

#     elif(ans.upper() == "C"):

        
#         print(f"CORRECT!!!⭕⭕")
#         grade =+ 25

#     else:
#         print("Wrong input")

#     return grade



# def main():
#     grade = 0
    
#     mark1 = que1(grade)
#     print("\n")
    
#     mark2 = que2(grade)
#     print("\n")
   
#     mark3 = que3(grade)
   
#     print("\n")
#     mark4 = que4(grade)
#     print("\n")
    


#     grade = mark1 + mark2 + mark3 + mark4

#     if grade < 100:
#         print("Bouns round")
#         mark5 = que5(grade)
#         print("\n")
        

#         new_grade = grade  + mark5
#         print(new_grade,"%")


#     else:
#         print(grade,"%")

        


# main()



# "Create a project that is able to change a word in a store sentence"

# sent = input("Enter you sentence:\n$ ")

# word = input("Enter the word you want to change:\n$ ")

# word2 = input("Enter the word you want to change it into:\n$ ")

# sent2 = sent.replace(word, word2)

# print(f"Your new sentence is:\nS {sent2}")











# list1 = [1, 0, 9, 1, 6, 3]
# list2 = ["Ivan", "Hikaru", "Kageyama", "Susune"]
# list1.sort()
# print(list1)


# for i in range(15):
#     i = i + 1
#     if(i % 3 == 0 and i % 5 == 0):
#         print("FizzBizz")
#         continue
    
#     elif(i % 3 == 0):
#         print("Fizz")
#         continue
    
#     elif(i % 5 == 0):
#         print("Bizz")
#         continue

#     else: 
#         print(i)



# Dictionaries

# my_dict = {
#     'name': "Lexy",
#     "age": 16,
#     "is_stu": True
# }

# my_dict["is_stu"] = False

# print(my_dict)


#while loops

# run = 1

# while run <= 10:
#     print(run)
#     run += 1


# forloops

# total = 0 
# num = [1, 2, 3, 4]

# for i in num:
#     total += i
   
# print("sum:" ,total)

# dic = {
#     "name": "lexy",
#     "age" : 34

# }


# for key, value in dic.items():
#     print(f"Key: {key}, Value: {value}")


## 2d list

# my_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in my_list:
#     for j in i:
#         print(j)


# try except
# try:
#     x = int(input("Enter a integer: "))
#     print(x)

# except:
#     print("ERROR!!! Input a  integer")




# file = open("Python Revision/paper.txt", "a")

# print(file.write("\nEdem"))



# class Person:
#     def __init__(self, name, age, isFemale):
#         self.name = name    
#         self.age = age   
#         self.isFemale = isFemale
        
# name = input("name: ")
# age = input("Age: ")
# isgirl = input("Are you a girl: (y / n): ")

# if isgirl.lower() == "yes" or isgirl.lower() == "y":
#     isgirl = True
# elif isgirl.lower() == "no" or isgirl.lower() == "n":
#     isgirl = False
# else:
#     print("not an option")


# p1 = Person(name, age, isgirl)

# del p1.isFemale

# print(p1.name)
# print(p1.age)





# class Person:
#     pass

"""
create a signup login  system.
sign up by creating
input username and password
then it send you to login with the username and password used to create an account if the input are 
different throw an error

i thin im going to save the data in a list in dictionary

"""

class Person:
    def __init__(self):
        self.box = {}

    def create(self):
        print("Create an Acount")
        username = input("Enter UserName: ")
        password = input("Enter password: ")

        self.box = [username, password]

        print("Account is Created Sucussfully")

    def login(self):
        print("Login Now")
        username = input("Enter UserName: ")
        password = input("Enter password: ")

        if self.box == [username, password] :
            print("Login  Correct")
        else:
            print("Wrong input")

p= Person()

p.create()
p.login()


        
