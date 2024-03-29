import LRU, FIFO, LFU, RND 
from random import * 
import matplotlib.pyplot as plt
import numpy as np

LRU_list = []
LFU_list = []
RND_list = []
FIFO_list = []

input_size = 30

for n in range(3, 11):

    tmp_LRU = 0
    tmp_LFU = 0
    tmp_RND = 0
    tmp_FIFO = 0
    for i in range(10):

        input_list = []

        for j in range(input_size):
            input_list.append(randint(0, 11))

        tmp_LRU += LRU.LRU_implement(input_list, n)
        tmp_LFU += LFU.LFU_implement(input_list, n)
        tmp_RND += RND.Random_implement(input_list, n)
        tmp_FIFO += FIFO.FIFO_implement(input_list, n)

    LRU_list.append(tmp_LRU / 10)
    LFU_list.append(tmp_LFU / 10)
    RND_list.append(tmp_RND / 10)
    FIFO_list.append(tmp_FIFO / 10)

index = [i for i in range(3,11)]
index = np.array(index)
width = 0.20

plt.bar(index, LRU_list, width, label = 'LRU')
plt.bar(index + width, LFU_list, width, label = 'LFU')
plt.bar(index + width * 2, FIFO_list, width, label = 'FIFO')
plt.bar(index + width * 3, RND_list, width, label = 'RND')

plt.title("Input Size : " + str(input_size))
plt.ylabel("HIT Ratio")
plt.xlabel("Slot Size")
plt.legend(loc='best')
plt.xticks(index + width / 2, index)

plt.show()