import numpy as np
import matplotlib.pyplot as plt
from style import W, save

def to_xy(p):
    cold,normal,hot = p
    return np.array([normal+0.5*hot, hot*np.sqrt(3)/2])

P = np.array([0.05,0.25,0.70])
eps = 0.2

V = np.eye(3)
ext = [(1-eps)*P+eps*v for v in V]
P_low = min(q[2] for q in ext)
P_up = max(q[2] for q in ext)

fig,ax = plt.subplots(figsize=(W,2.4))

tri = np.array([to_xy(v) for v in V]+[to_xy(V[0])])
ax.plot(tri[:,0],tri[:,1],'k-',lw=0.8)

cs = np.array([to_xy(q) for q in ext])
ax.fill(cs[:,0],cs[:,1],facecolor='lightgray',edgecolor='k',lw=0.8)

ax.plot(*to_xy(P),'ko',ms=3)
ax.annotate(r'$p$',to_xy(P),xytext=(0.40,0.30),ha='center',va='top',
            arrowprops=dict(arrowstyle='-',lw=0.5))
ax.annotate(r'$\mathcal{C}_{p,\epsilon}$, $\epsilon=%.1f$'%eps,
            0.5*(to_xy(ext[0])+to_xy(ext[1])),xytext=(-0.10,0.72),
            arrowprops=dict(arrowstyle='-',lw=0.5))

for val,lab in [(P_up,r'$\overline{P}(\mathrm{Hot})=%.2f$'%P_up),
                (P_low,'$P\u0332$'+r'$(\mathrm{Hot})=%.2f$'%P_low)]:
    y = val*np.sqrt(3)/2
    ax.plot([0.5*val,1.0],[y,y],'k--',lw=0.6)
    ax.text(1.03,y,lab,va='center')

ax.text(-0.02,-0.04,'Cold',ha='center',va='top')
ax.text(1.02,-0.04,'Normal',ha='center',va='top')
ax.text(0.5,0.9,'Hot',ha='center')

ax.set_xlim(-0.12,1.55)
ax.set_ylim(-0.12,0.95)
ax.set_aspect('equal')
ax.axis('off')

save(fig,'credal_set_figure')
