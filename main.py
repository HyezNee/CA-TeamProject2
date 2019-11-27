import LRU, FIFO, LFU, RND 
from datetime import datetime

def main():
    while(True):
        input_data = list(map(int, input("\n값 입력 : ").split()))
        slotcount = int(input("slotcount : "))

        starttime =datetime.now()
        LRU.LRU_implement(input_data,slotcount)
        print("LRU 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        FIFO.FIFO_implement(input_data,slotcount)
        print("FIFO 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        LFU.LFU_implement(input_data,slotcount)
        print("LFU 수행 시간 : ", (datetime.now()-starttime).microseconds)

        starttime = datetime.now()
        RND.Random_implement(input_data,slotcount)
        print("RND 수행 시간 : ", (datetime.now()-starttime).microseconds)


if __name__ == "__main__":
	main()        