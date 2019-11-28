def FIFO_implement(inputdata,slotcount):
    print("\nFIFO : ")

    n = len(inputdata)
    hit = 0
    a = []
    idx = 0

    for i in range(n):
        next_data = inputdata[i]

        if next_data in a:
            hit += 1
            print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}, HIT!!".format(i + 1, next_data, a))
            continue

        if len(a) < slotcount:
            a.append(next_data)

        else:
            # del(a[0])
            # a.append(next_data)
            a[idx % slotcount] = next_data  # 위의 코드도 FIFO의 과정에 부합하지만,
            idx += 1                        # 교수님이 수업 시간에 설명해주신 "순환 큐"의 내용을 반영해야 할 것 같아서 이렇게 해봤어요..!


        print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i + 1, next_data, a))

    print("H = {} / {} = {}".format(hit, n, hit / n))
    return hit / n
