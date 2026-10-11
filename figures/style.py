import matplotlib.pyplot as plt
from pathlib import Path

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['STIXGeneral']
plt.rcParams['mathtext.fontset']='stix'
plt.rcParams['font.size'] = 8
plt.rcParams['legend.fontsize']=7

W = 3.4

def save(fig,name):
    out = Path(__file__).parent/'output'
    out.mkdir(exist_ok=True)
    fig.savefig(out/(name+'.pdf'), bbox_inches='tight')
