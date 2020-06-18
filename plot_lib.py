import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def savefig(plt, filename):
    plt.savefig(filename + '.png')
    plt.savefig(filename + '.pdf')

def set_plot_style():
    #plt.style.use('bmh')
    #print(matplotlib.rcParams.keys())
    matplotlib.rcParams.update({
                               #'axes.grid': True,
                               #'axes.titlesize': 'medium',
                               'font.family': 'serif',
                               'font.serif': 'Palatino', #'Helvetica Neue',
                               'font.size': 33,
                               #'grid.color': 'w',
                               #'grid.linestyle': '-',
                               #'grid.alpha': 0.5,
                               #'grid.linewidth': 1,
                               'legend.frameon': False,
                               'legend.fancybox': False,
                               'legend.fontsize': 20,
                               'legend.numpoints': 1,
                               'legend.loc': 'best',
                               #'legend.framealpha': 0.7,
                               #'legend.handletextpad': 0.1,
                               #'legend.labelspacing': 0.2,
                               'lines.linewidth': 3,
                               'savefig.bbox': 'tight',
                               #'savefig.pad_inches': 0.02,
                               'text.usetex': True,
                               #'text.latex.preamble': r'\usepackage{txfonts}',
                               'xtick.labelsize': 30,
                               'ytick.labelsize': 30,
                               'xtick.direction': 'in',
                               'ytick.direction': 'in',
                               'axes.labelpad': 10,
                               'figure.autolayout': True,
                               })
    fig = plt.figure(figsize=(9.15, 8.7))
    ax = fig.add_subplot(1, 1, 1)
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(1.75)
    ax.minorticks_on()
    ax.tick_params('both', length=15, width=1.5, which='major', pad=10, bottom=True, top=True, left=True, right=True)
    ax.tick_params('both', length=10, width=1.3, which='minor', pad=10, bottom=True, top=True, left=True, right=True)
    return fig, ax

def str_to_Z(s):
    if (s == 'H'):
        return 1
    elif (s == 'He'):
        return 2
    elif (s == 'Li'):
        return 3
    elif (s == 'Be'):
        return 4
    elif (s == 'B'):
        return 5
    elif (s == 'C'):
        return 6
    elif (s == 'N'):
        return 7
    elif (s == 'O'):
        return 8
    elif (s == 'F'):
        return 9
    elif (s == 'Ne'):
        return 10
    elif (s == 'Na'):
        return 11
    elif (s == 'Mg'):
        return 12
    elif (s == 'Al'):
        return 13
    elif (s == 'Si'):
        return 14
    elif (s == 'P'):
        return 15
    elif (s == 'S'):
        return 16
    elif (s == 'Cl'):
        return 17
    elif (s == 'Ar'):
        return 18
    elif (s == 'K'):
        return 19
    elif (s == 'Ca'):
        return 20
    elif (s == 'Sc'):
        return 21
    elif (s == 'Ti'):
        return 22
    elif (s == 'V'):
        return 23
    elif (s == 'Cr'):
        return 24
    elif (s == 'Mn'):
        return 25
    elif (s == 'Fe'):
        return 26
    elif (s == 'Co'):
        return 27
    elif (s == 'Ni'):
        return 28
    elif (s == 'Cu'):
        return 29
    elif (s == 'Zn'):
        return 30
    else:
        print (s, 'is not found')
    
def str_to_time(t):
    if (t == 'ms'):
        return 1e-3
    elif (t == 's'):
        return 1.
    elif (t == 'm'):
        return 60.
    elif (t == 'h'):
        return 3600.
    elif (t == 'd'):
        return 3600. * 24.
    elif (t == 'y'):
        return 3600. * 24. * 365.25
    else:
        print (t, 'is not found')
    return 0

def read_ghosts(filename):
    Zp = []
    Ap = []
    tdecay = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines[1:]:
        line = line.split()
        Zp.append(str_to_Z(line[0]))
        Ap.append(int(line[1]))
        T = float(line[5])
        T *= str_to_time(line[6])
        tdecay.append(T)
    return Zp, Ap, tdecay

def read_child(filename):
    Zc = []
    Ac = []
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines[1:]:
        line = line.split()
        Zc.append(str_to_Z(line[2]))
        Ac.append(int(line[3]))
    return Zc, Ac
