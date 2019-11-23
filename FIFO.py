def FIFO_implement(inputdata,slotcount):
    print("\nFIFO : ")

    n = len(inputdata)
    hit = 0
    a = []

    for i in range(n):
        next_data = inputdata[i]

        if next_data in a:
            hit += 1
            print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}, HIT!!".format(i + 1, next_data, a))
            continue

        if len(a) < slotcount:
            a.append(next_data)

        else:
            del(a[0])
            a.append(next_data)

        print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i + 1, next_data, a))

    print("H = {} / {} = {}".format(hit, n, hit / n))
    return hit / n
