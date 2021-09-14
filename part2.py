#not
#and(F)
#or(T)
x = 7
y = 8
z = 0
result1 = x == y
result2 = y > x
result3 = z < x + 2
result4= result1 and result2
print(result4)
print(not (True and False or True))


x = input('Name: ')
if x == 'Bianca':
    print('You are great!')
elif x == 'Dragos':
    print('You are big')
elif x == 'Andrei':
    print('You are small')
else:
    print('You are ok')


#len(lungime)
#.append(adauga la var x);extend;add;remove
#pop(elimina; 0-primul element,1-...)
x = [4, True, 'hi']
y = 'hello'
print(len(x), len(y))

x.append('hello')
print(x)

print(x.pop(0))
print(x)

x[2] = 'car'
print(x)

#for loops
#(start,stop,step)

for i in range(10, -1, -1):
    print(i)

x = [3,6,8,45,32,5]
for i, element in enumerate(x):
    print(i, element)
print("Bia")






