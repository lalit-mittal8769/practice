s = input()
counter=0
values =[]
for i in s:
    for j in s:
        if i==j:
            counter+=1
    values.append(i)
    values.append(counter)
    counter=0
print(f'{len(values)}')
print(f'{values}')
x=0
y=0

for i in values[x:len(values):2]:
    for j in values[x+2:len(values):2]:
        if i==j:
            print('ok')
            del values[x+1]
            del values[x]
    x+=2
print(f'{values}')
