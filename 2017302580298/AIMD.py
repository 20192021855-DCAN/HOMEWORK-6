import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
import numpy as np

time = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
cwnd = [1]
mwnd = 20
ssthresh = 16
i = 0
ssthreshes = [[ssthresh,0]]

def AdditiveIncrease():
    global i
    while i < 19 and cwnd[i]+1 <= mwnd:
        cwnd.append(cwnd[i]+1)
        i += 1


def SlowStart():
    global i
    while i < 19 and 2*cwnd[i] < ssthresh:
        cwnd.append(2*cwnd[i])
        i += 1
    if i < 19:
        cwnd.append(ssthresh)
        i += 1

def reno():
    global i
    cwnd.append(ssthresh)
    i += 1

def tahoe():
    global i
    cwnd.append(1)
    i += 1

def MultiplicativeDecrease():
    global i,ssthresh,ssthreshes
    ssthresh = int(cwnd[i]/2)
    ssthreshes.append([ssthresh,i+2])

def AIMD_Tahoe():
    while True:
        if i > 18: break
        SlowStart()
        if i > 18: break
        AdditiveIncrease()
        if i > 18: break
        MultiplicativeDecrease()
        if i > 18: break
        tahoe()


def AIMD_Reno():
    SlowStart()
    while True:
        if i > 18: break
        AdditiveIncrease()
        if i > 18: break
        MultiplicativeDecrease()
        if i > 18: break
        reno()


def reset():
    global ssthresh,ssthreshes,cwnd,i
    ssthresh = 16
    ssthreshes = [[ssthresh,0]]
    cwnd = [1]
    i = 0

def display():
    AIMD_Tahoe()
    x1 = time
    y1 = cwnd
    plt.plot(x1,y1,label="FTP Tahoe", marker='o', ms=4, mfc='w')
    for a, b in zip(x1, y1):
        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)

    reset()
    AIMD_Reno()
    x2 = time
    y2 = cwnd
    plt.plot(x2,y2,label="FTP Reno",marker='o', ms=3,linestyle=':')
    for a, b in zip(x2, y2):
        plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)

    for thresh in ssthreshes:
        if thresh[1] == 0:
            plt.hlines(thresh[0], -0.5, 9,label='origin ssthresh')  # 初始ssthresh
        else:
            plt.hlines(thresh[0], 9, 19,linestyle=':',label='new ssthresh')  # 新的ssthresh

    plt.xlabel("Transmission round")
    plt.ylabel('cwnd')

    x_major_locator = MultipleLocator(1)
    # 把x轴的刻度间隔设置为1，并存在变量里
    y_major_locator = MultipleLocator(1)
    # 把y轴的刻度间隔设置为10，并存在变量里
    ax = plt.gca()
    # ax为两条坐标轴的实例
    ax.xaxis.set_major_locator(x_major_locator)
    # 把x轴的主刻度设置为1的倍数
    ax.yaxis.set_major_locator(y_major_locator)
    plt.xlim(-0.5, 22)
    # 把x轴的刻度范围设置为-0.5到22，因为0.5不满一个刻度间隔，所以数字不会显示出来，但是能看到一点空白
    plt.ylim(-0.5, 22)
    # 把y轴的刻度范围设置为-5到22

    plt.title('TCP Congestion control')
    plt.legend()
    plt.show()

display()