import LRU, FIFO, LFU, RND
from random import *
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

LRU_list = []
LFU_list = []
RND_list = []
FIFO_list = []

input_size = 100

for n in range(3, 11):

    time_LRU = 0
    time_LFU = 0
    time_RND = 0
    time_FIFO = 0
    for i in range(10):

        input_list = []

        for j in range(input_size):
            input_list.append(randint(0, 11))

        starttime = datetime.now()
        LRU.LRU_implement(input_list, n)
        tmpTime_LRU = (datetime.now()-starttime).microseconds

        starttime = datetime.now()
        LFU.LFU_implement(input_list, n)
        tmpTime_LFU = (datetime.now()-starttime).microseconds

        starttime = datetime.now()
        RND.Random_implement(input_list, n)
        tmpTime_FIFO = (datetime.now()-starttime).microseconds

        starttime = datetime.now()
        FIFO.FIFO_implement(input_list, n)
        tmpTime_RND = (datetime.now()-starttime).microseconds

        time_LRU += tmpTime_LRU
        time_LFU += tmpTime_LFU
        time_RND += tmpTime_RND
        time_FIFO += tmpTime_FIFO

    LRU_list.append(time_LRU / 10)
    LFU_list.append(time_LFU / 10)
    RND_list.append(time_RND / 10)
    FIFO_list.append(time_FIFO / 10)

index = [i for i in range(3,11)]
index = np.array(index)
width = 0

plt.plot(index, LRU_list, label = 'LRU')
plt.plot(index, LFU_list, label = 'LFU')
plt.plot(index, FIFO_list, label = 'FIFO')
plt.plot(index, RND_list, label = 'RND')

plt.scatter(index, LRU_list)
plt.scatter(index, LFU_list)
plt.scatter(index, FIFO_list)
plt.scatter(index, RND_list)

plt.title("Input Size : " + str(input_size))
plt.ylabel("Excution Time")
plt.xlabel("Slot Size")
plt.legend(loc='best')
plt.xticks(index + width / 2, index)

plt.show()