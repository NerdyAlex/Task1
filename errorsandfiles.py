try:
    age = int(input('Enter your age: '))
    print(age,'is your age.')
except:
    print('''That's not your age..''')
else:
    print('Nothing went wrong')
finally:
    print('Finished loading....')