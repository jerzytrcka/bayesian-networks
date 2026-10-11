import numpy as np
import matplotlib.pyplot as plt
from style import W, save

def trap(x,a,b,c,d):
    y = np.ones_like(x)
    if b>a: y = np.minimum(y,(x-a)/(b-a))
    if d > c: y = np.minimum(y, (d-x)/(d-c))
    return np.clip(y,0,1)

x = np.linspace(40,130,1000)
T = 99

fig,ax = plt.subplots(figsize=(W,2))
ax.plot(x,trap(x,40,40,60,75),'k-',label='Cold')
ax.plot(x, trap(x,60,75,90,105),'k--',label='Normal')
ax.plot(x,trap(x,90,105,130,130), 'k:', label='Hot')

ax.axvline(T,color='gray',lw=0.8)
for p in [(60,75,90,105),(90,105,130,130)]:
    m = trap(np.array([T]),*p)[0]
    ax.plot(T,m,'ko',ms=3)
    ax.text(T+2,m,'%.1f'%m,va='center')

ax.set_xlim(40,130)
ax.set_ylim(0,1.05)
ax.set_xlabel('Coolant temperature (°C)')
ax.set_ylabel('Membership degree')
ax.legend(loc='upper center',bbox_to_anchor=(0.5,1.2),ncol=3, frameon=False)

save(fig,'fuzzy_membership_functions')
