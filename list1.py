'''mylist = list(("apple", "banana", "grape", "orange", "mango"))
num = [25, 6 ,71,4,5,7]

mylist.insert(3, "cherry")
print(mylist)
print(len(num))





name = ["anny", "lex", 2, True, 0.5, "mike", 'ixy']
print(type(name[3]))
name[0] = "Anny"
name[1] = "Lex"
name[6] = 'Ixy'
name[5] = 'Mike'
print(name)


name1 = tuple((True, 1.23, 'anny'))
print(type(name1))
'''

list1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i in list1:
    for small in i:
        print(small)