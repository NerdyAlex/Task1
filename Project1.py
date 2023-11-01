print('Create your account')
username = input('Input Username: ')
password = input('Input password: ')
print("User ", username.capitalize(), " was created sucessfully")

print('LogIn Now')

username1 = input('Input Username: ')
password1 = input('Input password: ')

if username  == username1:
    print("User logged in sucessfully")

if password == password1:
    print("User logged in sucessfully")
else:
    print("Incorrect username or password")