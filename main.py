import LRU, FIFO, LFU, RND 

def main():
    while(True):
        input_data = list(map(int, input("\n값 입력 : ").split()))
        slotcount = int(input("slotcount : "))

        print("\nLRU : ")
        LRU.LRU_implement(input_data,slotcount)
        print("\nFIFO : ")
        FIFO.FIFO_implement(input_data,slotcount)
        print("\nLFU : ")
        LFU.LFU_implement(input_data,slotcount)
        print("\nRandom : ")
        RND.Random_implement(input_data,slotcount)

if __name__ == "__main__":
	main()        