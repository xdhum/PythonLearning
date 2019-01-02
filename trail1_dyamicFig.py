

'''
Created on 2018��

@author: Xie Ding

'''

import numpy as np
#import pylab as plt

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
fig.set_tight_layout(True)

angle_cir = [i*np.pi/180 for i in range(0,361)]
xp = np.cos(angle_cir)
yp = np.sin(angle_cir)
plt.plot(xp,yp)
#plt.plot(0,0,'bo-',lw=0.5)

print("xp[i]",xp[5])
#point_line,=plt.plot(x1[0],y1[0],'or')

xdata, ydata = [], []
line1, = ax.plot([],[], 'ro', animated=False)
x_cos = np.arange(0,10,1)
y_cos = np.zeros(1,10)

plt.plot(x_cos,y_cos)
plt.show()
lx1, = ax.plot(x_cos,y_cos,'g-')
ly1, = ax.plot([],[], 'g-', animated=False)
#  line1, = ax.plot([],[], 'ro-')
def init():
    ax.set_xlim(-4, 2*np.pi)  #设置x轴的范围pi代表3.14...圆周率，
    #ax.set_ylim(-1, 1)       #设置y轴的范围
    line1.set_data([],[])
    return line1,ax               #返回曲线

def update(n):
    #xdata.append(x1[n])         #将每次传过来的n追加到xdata中
    #ydata.append(y1[n])
    #xdata = np.cos(n)-1.5         #将每次传过来的n追加到xdata中
    #ydata = np.sin(n)
    xpoint = xp[n]
    ypoint = yp[n]
    print("xpoint",xpoint)
    if xpoint == 0:
        x_cos = 0
        y_cos = 0
    elif xpoint>0:
        x_cos = np.arange(0,xpoint, xpoint/10)
        y_cos = np.zeros((1,10))
#        ysin = np.arange(0,ypoint, ypoint/10)
#        xsin = np.zeros((1,ysin.size))
    elif xpoint<0:
        x_cos = np.arange(0, xpoint, xpoint/10)
        y_cos = np.zeros((1,10))
    print("x_cos",x_cos)
    print("y_cos",y_cos)
    line1.set_data(xpoint, ypoint)    #重新设置曲线的值
    lx1.set_data(x_cos,y_cos)    #重新设置曲线的值
    return line1,lx1

plt.axis('equal')#避免比例压缩为椭圆
#这里的frames在调用update函数是会将frames作为实参传递给“n”
#ani = FuncAnimation(fig, update, frames=angle_cir,init_func=init, interval=0.001,blit=True)
ani = FuncAnimation(fig, update, frames=range(0, len(xp)),interval=1, blit=True)


plt.show()
print("End!!!")


