import LRU, FIFO, LFU, RND
from random import *
import matplotlib.pyplot as plt
import numpy as np

LRU_list = []
LFU_list = []
RND_list = []
FIFO_list = []

input_size = 100

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
plt.ylabel("HIT Ratio")
plt.xlabel("Slot Size")
plt.legend(loc='best')
plt.xticks(index + width / 2, index)

plt.show()