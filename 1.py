a=input('Введите имя: ')
b=input('Введите фамилию: ')
c=int(input('Введите год рождения: '))
print(a,b,c,sep='_')
a,b=b,a
c=c+60
print(a,b,c,sep='_')
