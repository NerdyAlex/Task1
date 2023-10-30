try:
    num = int(input('Enter your digit: '))
    print(num,'is a number.')
except:
    print('''That's not a number.''')
else:
    print('Nothing went wrong')
finally:
    print('Loaded....')