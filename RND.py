from random import *

def Random_implement(inputdata,slotcount):
    
    n = len(inputdata)
    hit = 0
    a = []

    for i in range(n):
        next_data = inputdata[i]

        if next_data in a:
            hit += 1
            print("Round#{0} -> 현재 캐쉬 상태 : {1}, HIT!!".format(i+1, a))
            continue

        if len(a) < slotcount:
            a.append(next_data)

        else:
            random_number = randint(0, slotcount-1)
            a[random_number] = next_data

        print("Round#{0} -> 현재 캐쉬 상태 : {1}".format(i+1, a))

    print(hit, hit/n)