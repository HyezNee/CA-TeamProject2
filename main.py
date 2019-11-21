import LRU, FIFO, LFU, RND 

def main():
    while(True):
        input_data = list(map(int, input("값 입력 : ").split()))
        slotcount = int(input("slotcount : "))

        LRU.LRU_implement(input_data,slotcount)
        FIFO.FIFO_implement(input_data,slotcount)
        LFU.LFU_implement(input_data,slotcount)
        RND.Random_implement(input_data,slotcount)

if __name__ == "__main__":
	main()        