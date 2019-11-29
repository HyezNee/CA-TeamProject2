from random import *

def Random_implement(inputdata,slotcount):

    n = len(inputdata)
    hit = 0
    a = []

    for i in range(n):
        next_data = inputdata[i]

        if next_data in a:
            hit += 1
            continue

        if len(a) < slotcount:
            a.append(next_data)

        else:
            random_number = randint(0, slotcount-1)
            a[random_number] = next_data


    return hit / n