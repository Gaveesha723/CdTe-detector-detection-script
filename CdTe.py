import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
from scipy.signal import savgol_filter
import mplcursors

time=np.arange(0,20,5)
x=[5]*len(time)
result=[]
for t in time:
    if t==0:
        result.append(0)
    else:
        t_=np.arange(0,t+1,5)
        y=[5]*len(t_)
        r=simpson(y,t_)
        result.append(r)

print(result[-1])

check=simpson(x,time)
print(check)
plt.plot(time,x)
plt.plot(time,result)
plt.show()