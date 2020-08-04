#Code for selecting all natural numbers less than 10 that are multiples of 3 and 5 and finding their sum.
#January , 2019


#Код для выделения всех натуральных чисел меньше 10 которые кратны 3 и 5 и нахождения их  суммы.
#Январь 2019


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
