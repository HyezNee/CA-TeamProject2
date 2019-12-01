import random

def NEW_implement(inputdata,slotcount):
    #print("\nLRU : ")

    n = len(inputdata)
    hit = 0
    datas = []
    counts = []

    for i in range(n):
        next_data = inputdata[i]

        if next_data in datas:
            hit += 1
            counts[datas.index(next_data)] = -1
            for index in range(len(counts)):
                counts[index] += 1
            #print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}, HIT!!".format(i + 1, next_data, list(zip(datas, counts))))
            continue

        if len(datas) < slotcount:
            datas.append(next_data)
            counts.append(-1)
            for index in range(len(counts)):
                counts[index] += 1

        else:
            choice_data = random.choices(datas, weights=counts, k=1)[0]
            datas[datas.index(choice_data)] = next_data
            counts[datas.index(next_data)] = -1
            for index in range(len(counts)):
                counts[index] += 1

        #print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i + 1, next_data, list(zip(datas,counts))))

    #print("H = {} / {} = {}".format(hit, n, hit/n))
    return hit / n