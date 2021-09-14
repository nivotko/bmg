N = int(input())
sum = 0
for i in range(1,N+1):
    if i < N:
        if i % 15 == 0:
            print("BMG", end = " , ")
        elif i % 15 == 14:
            print(i, end=" , ")
            sum += i
        else:
            print(i, end=" + ")
            sum += i
    else:
        if i % 15 == 0:
            print("BMG", end = " = ")
        else:
            print(i, end=" = ")
            sum += i
print(sum)
