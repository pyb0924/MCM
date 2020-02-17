import scipy.integrate as spi
import numpy as np
import matplotlib.pyplot as plt

# define time, constants and initial statess
N1 = [x for x in range(3000, 6000, 500)]  # initial N
P_env = 500  # initial P_env
E = 95  # E
alpha = 0.13  # N1:amount of waste
lamda = 0.15
r = 1000
beta = 3e-4
t_range = np.arange(0, 300)
INPUT = []
for i in range(6):  # for each E, create input series
    INPUT.append([N1[i], P_env, E])


def diff_eqs(INP, t):
    y = np.zeros(3)
    v = INP
    y[0] = v[2] - alpha * v[1]
    K = lamda * v[0] - np.exp(beta * v[0])
    y[1] = r * v[1] * (1 - v[1] / K)
    y[2] = 0
    return y

# Ploting


def draw(ans):
    plt.plot(ans[:, 0], '-r', label="Amount of Waste")
    plt.plot(ans[:, 1], '-g', label="Amount of microbe")


style = ['-r', '-g', '-y', '-b', '-k', '-c']
# run and draw (for each different E)
for i in range(6):
    RES = spi.odeint(diff_eqs, INPUT[i], t_range)
    plt.plot(RES[:, 0], style[i], label="N=" + str(N1[i]))


plt.legend(loc="best")
# plt.title('Influence of different initial E')
plt.xlabel('Time(year)')
plt.ylabel('N(10^6t)')
plt.savefig('figure\sensitivity_analysis', dpi=900)
plt.show()
