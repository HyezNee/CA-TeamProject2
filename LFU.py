import heapq

def LFU_implement(inputdata,slotcount):
    n = len(inputdata)
    hit = 0
    datas = []  # 슬롯 역할을 할 힙

    for i in range(n):
        next_data = inputdata[i]
        uniqueNum = i   # uniqueNum : heapq 모듈이 두번 이상의 value도 같이 정렬시켜버리므로 그것을 방지하기 위해.
        if next_data in [item[2] for item in datas]:  # 캐시 적중
            current = [item for item in datas if item[2] == next_data][0]   # next_data를 튜플의 세 번재 값(데이터값)으로 갖는 특정 튜플(슬롯) 찾기
            oldIdx = datas.index(current)
            datas[oldIdx]=(current[0]+1, current[1], current[2])    # 해당 슬롯의 카운터를 1 증가
            heapq._siftup(datas, oldIdx)    # 힙 갱신
            hit += 1
            print("Round#{} -> [{}] 현재 캐쉬 상태 : {}, HIT!!".format(i + 1, next_data, [(item[2], item[0]) for item in datas]))
        else: # 캐시 미스
            if len(datas) < slotcount:  # 슬롯이 다 차지 않았을 때
                heapq.heappush(datas, (1, uniqueNum, next_data))   # 슬롯에 데이터 추가. 카운터는 1로 초기화
            else:   # 슬롯이 다 찼을 때
                heapq.heappop(datas)
                heapq.heappush(datas, (1, uniqueNum, next_data))   # 슬롯에 데이터 교체. 카운터는 1로 초기화
            print("Round#{} -> [{}] 현재 캐쉬 상태 : {}".format(i + 1, next_data, [(item[2], item[0]) for item in datas]))

    print("H = {} / {} = {}".format(hit, n, hit/n))