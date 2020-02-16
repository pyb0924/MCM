import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

# define time, constants and initial statess
N1 = 4977
N2 = 500
E = 100#114.7
alpha = 0.13
k = 0.15
r = 1000
beta=3e-4
t_range = np.arange(0,500)
INPUT = [N1, N2]  # N1:amount of waste, N2:amount of microbe


def min(a, b):
    if a > b:
        return b
    else:
        return a


def diff_eqs(INP, t):
    y = np.zeros(2)
    v = INP
    y[0] = E - alpha * v[1]
    K=k*v[0]-np.exp(beta*v[0])
    y[1]=r*v[1]*(1-v[1]/K)
    return y

# Ploting
def draw(ans):
    plt.plot(ans[:, 0], '-r', label="Amount of Waste")
    plt.plot(ans[:, 1], '-g', label="Amount of microbe")
    plt.legend(loc=0)
    plt.title('Influence of different initial amount of waste')
    plt.xlabel('Time(year)')
    plt.ylabel('Amount')
    plt.show()

RES = spi.odeint(diff_eqs, INPUT, t_range)
draw(RES)

