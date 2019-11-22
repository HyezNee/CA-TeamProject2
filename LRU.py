def LRU_implement(inputdata,slotcount):
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
            print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}, HIT!!".format(i + 1, next_data, list(zip(datas, counts))))
            continue

        if len(datas) < slotcount:
            datas.append(next_data)
            counts.append(-1)
            for index in range(len(counts)):
                counts[index] += 1

        else:
            max_count = 0
            max_count_index = 0
            for index in range(len(counts)):
                if counts[index] > max_count:
                    max_count = counts[index]
                    max_count_index = index
            datas[max_count_index] = next_data
            counts[max_count_index] = -1
            for index in range(len(counts)):
                counts[index] += 1

        print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i + 1, next_data, list(zip(datas,counts))))

    print("H = {} / {} = {}".format(hit, n, hit/n))