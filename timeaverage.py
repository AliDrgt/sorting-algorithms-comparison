import numpy as np
import matplotlib.pyplot as plt 


y= [100,1000,10000,50000]



q2 = [352,6274,77393,528969]
s2 = [100,1000,10000,50000]
m2 = [871,11975,153615,884463]


plt.plot(y,m2)
plt.plot(y,q2)
plt.plot(y,s2)

plt.ylabel("Number of Assingments",fontsize=15)
plt.legend(["Merge Sort","Quick Sort","Selection Sort"])
plt.xlabel("Input Size",fontsize=15)
#plt.xticks(np.arange(0,25,5))
plt.grid()
plt.show()

