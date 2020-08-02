#Код для выделения всех натуральных чисел меньше 10 которые кратны 3 и 5 и нахождения их  суммы.January 18,2019
#January , 2020 
ten = int(10)
three = int(3)
five = int(5)
simm = int(0)
i = int(1)
v = int(0)

while i<ten:
    v=i%three
    if v == 0:
        simm=i+simm
        v=0
    elif v>0:
        pass
    v=i%five
    if v == 0:
        simm=i+simm
        v=0
    elif v>0:
        pass
    i=i+1


print(simm)
