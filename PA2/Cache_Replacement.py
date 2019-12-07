import heapq
from random import *
import random
from datetime import datetime

def LRU_implement(inputdata,slotcount):

    print("\nLRU : ")

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
    return hit / n


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



def LFU_implement(inputdata,slotcount):
    print("\nLFU : ")

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
    return hit / n


def Random_implement(inputdata,slotcount):
    print("\nRandom : ")

    n = len(inputdata)
    hit = 0
    a = []

    for i in range(n):
        next_data = inputdata[i]

        if next_data in a:
            hit += 1
            print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}, HIT!!".format(i+1, next_data, a))
            continue

        if len(a) < slotcount:
            a.append(next_data)

        else:
            random_number = randint(0, slotcount-1)
            a[random_number] = next_data

        print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i+1, next_data, a))

    print("H = {} / {} = {}".format(hit, n, hit/n))
    return hit / n


def NEW_implement(inputdata,slotcount):
    print("\nLRU : ")

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
            choice_data = random.choices(datas, weights=counts, k=1)[0]
            datas[datas.index(choice_data)] = next_data
            counts[datas.index(next_data)] = -1
            for index in range(len(counts)):
                counts[index] += 1

        print("Round #{0} -> [{1}] 현재 캐쉬 상태 : {2}".format(i + 1, next_data, list(zip(datas,counts))))

    print("H = {} / {} = {}".format(hit, n, hit/n))
    return hit / n


def main():
    while(True):
        input_data = list(map(int, input("\n값 입력 : ").split()))
        slotcount = int(input("slotcount : "))

        starttime =datetime.now()
        LRU_implement(input_data,slotcount)
        print("LRU 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        FIFO_implement(input_data,slotcount)
        print("FIFO 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        LFU_implement(input_data,slotcount)
        print("LFU 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        Random_implement(input_data,slotcount)
        print("RND 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        NEW_implement(input_data, slotcount)
        print("NEW 수행 시간 : ", (datetime.now() - starttime).microseconds)


if __name__ == "__main__":
	main()