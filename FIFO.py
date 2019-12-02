def FIFO_implement(inputdata,slotcount):
    print("\nFIFO : ")
    # n 입력받는  데이터의 갯수
    n = len(inputdata)
    hit = 0  # hit 갯수
    a = [] # 현재 캐쉬 상태 리스트
    idx = 0 # 순환 큐 형태를 위한 변수- 가장 오래된 캐쉬 슬롯 지정

    for i in range(n): # 데이터의 갯수 만큼 입력 수행
        next_data = inputdata[i]

        if next_data in a: # 캐시 안에 있을 시에는
            hit += 1 
            print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}, HIT!!".format(i + 1, next_data, a))
            continue 
        # 캐시 안에 없을 때
        if len(a) < slotcount: # 캐시 슬롯의 빈자리 존재
            a.append(next_data) # 캐시 삽입

        else: # 빈 자리가 없을 떄
            a[idx % slotcount] = next_data # 가장 오래된 캐시슬롯에 캐시 삽입
            idx += 1

        #현재 상태 출력
        print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i + 1, next_data, a))

    print("H = {} / {} = {}".format(hit, n, hit / n))
    return hit / n
