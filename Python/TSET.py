n = 3


lst1 = [x for x in range(n)]
lst2 = []

for num, i in enumerate(lst1):

    if num == 0:
        lst1[num] = 1

    lst2.append(num + num+1)


print(lst2)
