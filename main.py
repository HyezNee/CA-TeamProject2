import LRU, FIFO, LFU, Random

def main():
    while(True):
        data = input("입력할 데이터 : ")
        data=data.split(" ")
        slotcount=input("slotcount : ")

        LRU.LRU_implement(data,slotcount)
        FIFO.FIFO_implement(data,slotcount)
        LFU.LFU_implement(data,slotcount)
        Random.Random_implement(data,slotcount)