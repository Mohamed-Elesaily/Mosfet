
import matplotlib.pyplot as plt 
import numpy as np


V = np.linspace(0, 1, 1000)
V1 = np.linspace(0, 2, 1000)
V2 = np.linspace(0, 3, 1000)


vsat1=np.linspace(1,3,1000)
vsat2=np.linspace(2,4,1000)
vsat3=np.linspace(3,6,1000)

Isat2=2.28 + vsat2*0
Isat3=3.42 + vsat3*0
Isat1=0.855 + vsat1*0
I=5.7*0.1*(2 *V - 0.5 * V**2)
I1=5.7*0.1*(3*V1 - 0.5*V1**2)

I2=5.7*0.1*(3.5*V2 - 0.5*V2**2)

plt.plot(vsat1,Isat1,"blue")
plt.plot(vsat2,Isat2,"orange")
plt.plot(vsat3,Isat3,"green")
plt.plot(V,I,"blue")
plt.plot(V1,I1,"orange")
plt.plot(V2,I2,"green")
plt.xlabel('Vds(V)', fontsize=10)
plt.ylabel('iD(mA)', fontsize=10)
plt.show()