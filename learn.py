#conditionals
a = 30 
b = 30 
if a<b:
    print('b is greater')
elif a>b:
    print('a is greater')
else:
        print('a is equal to b')

#nested if
a = 60
b = 20
if a>b:
    print('a is greater than b')
    if a>50:
        print('also a is greater than 50')
        if a>75:
            print('and a is greater than 75')
if b>a:
    print('b is greater than a')

#loops
a =True
i = 0
while a:
    i=i+1
    print(i)
    if i==5:
      a = False

a = [23,34,56,67,77]
i = 0
while i<len(a):
    print(a[i])
    i += 1

for i in range(1,11):
    if(i==5):
        continue
    if(i==7):
        continue
    print(i)

for i in range(1,11):
        if(i<7):
          pass
        else:
          print(i)




