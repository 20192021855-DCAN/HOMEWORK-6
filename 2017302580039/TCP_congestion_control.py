import numpy as np
from matplotlib import pyplot as plt

# 拥塞控制模拟类
class simulator:
    def __init__(self, ssthresh):
        self.ssthresh = ssthresh
        self.current_y = 1
        self.x = []
        self.y = []
        self.ssthreshs = []
        self.start_position = 0

    # 慢开始算法
    def slow_start(self):
        i = 0
        while 2**i <= self.ssthresh:
            self.x.append(i+self.start_position)
            self.y.append(2**i)
            self.ssthreshs.append(self.ssthresh)
            self.current_y = 2**i
            i += 1
        if(self.current_y == self.ssthresh):
            self.start_position = self.start_position + i - 1
        else:
            self.x.append(i + self.start_position)
            self.y.append(self.ssthresh)
            self.ssthreshs.append(self.ssthresh)
            self.current_y = self.ssthresh
            self.start_position = self.start_position + i

    # 线性增长
    def linear_growth(self,dict):
        cwnd = dict['cwnd']
        if(dict['event'] == "拥塞超时重传"):
            pass
        elif (dict['event'] == "收到三个重复确认"):
            pass
        else:
            self.start_position -= 1
        while self.current_y < cwnd:
            self.current_y += 1
            self.start_position += 1
            self.x.append(self.start_position)
            self.y.append(self.current_y)
            self.ssthreshs.append(self.ssthresh)
        self.start_position += 1
        if(dict['event'] == "拥塞超时重传"):
            self.current_y = 1
        else:
            self.current_y = int(cwnd / 2)-1
        self.ssthresh = int(cwnd / 2)

    # 绘制图像
    def plot(self):
        plt.plot(self.x, self.y, linewidth = 2.5, label="cwnd")
        plt.plot(self.x, self.ssthreshs,color='r', linestyle=':', linewidth=2.5, label="ssthresh")
        plt.legend(loc='upper right')
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.xlabel('传输轮次')
        plt.ylabel('拥塞窗口 cwnd')
        plt.title('TCP 的拥塞控制')
        plt.yticks(range(0, 25, 1))
        plt.xticks(range(0, 27, 1))
        plt.savefig('./plot.jpg')
        plt.show()


if __name__ == '__main__':
    '''
    模拟的过程为：
    ·先模拟：超时重传
    ·再模拟：快重传和快恢复
    '''
    # 初始化 ssthresh 为16
    initial_ssthresh = 16
    simulator = simulator(initial_ssthresh)
    # 慢开始算法
    simulator.slow_start()
    # 拥塞避免算法，当传输到 cwnd = 24 的时候发生事件：拥塞超时重传
    simulator.linear_growth({'event': "拥塞超时重传", 'cwnd': 24})
    # 慢开始传输
    simulator.slow_start()
    # 快重传,当传输到 cwnd = 16 的时候发生事件：收到三个重复确认
    simulator.linear_growth({'event': "收到三个重复确认", 'cwnd': 16})
    # 采用快恢复进行正常传输
    simulator.linear_growth({'event': "正常传输", 'cwnd': 12})
    # 绘制折线图
    simulator.plot()


