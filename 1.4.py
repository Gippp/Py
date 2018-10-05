
n=int(input("Введите количество команд "))
print("Вводите команды в виде: u(up), d(down), l(left),r(right), затем"
        "количество шагов: u1, u2, d3 и тд")
coor=[0,0]
for i in range(0,n):
    com=input("Введите команду ")
    napr=com[0]
    shag=int(com[1])
    if napr =='u':
        coor[1]+=shag
    elif napr=='d':
        coor[1]-=shag
    elif napr=='l':
        coor[0]-=shag
    elif napr =='r':
        coor[0]+=shag
    else:
        print("Вы все испортили =( Несуществующая команда")
        exit(-1)

print("Конечная точка гнома=",coor) 
