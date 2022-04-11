import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
alpha = 1.0
beta = 1.0
x = np.arange (0.01, 1.0, 0.01)
y2 = stats.beta.pdf(x, alpha, beta)
y3 = stats.beta.pdf(x, 0.5*alpha, 0.5*beta)
y4 = stats.beta.pdf(x, 2.5*alpha, 1.5*beta)
plt.plot(x,y2, label = r" $\alpha = 1.0, beta = 1.0$")
plt.plot(x,y3, linestyle = ':', label = r" $\alpha = 0.5, beta = 0.5$")
plt.plot(x,y4, linestyle = '--', label = r" $\alpha = 2.5, beta = 1.5$")
plt.legend()
plt.show()

