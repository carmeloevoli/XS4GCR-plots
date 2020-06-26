import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches

import plot_lib as plib

year = 3600. * 24. * 365.25
kyr = 1e3 * year
Myr = 1e6 * year

def gamma(Z, A, R):
    az2 = float(A * A) / float(Z * Z)
    return np.sqrt(az2 * (R / 0.938)**2. + 1.)

def plot_decay(ax, Z, A, R, tdec, label, color):
    y = tdec * gamma(Z, A, R)
    ax.plot(R, y / (1e3 * year), label=label, color=color)

def plot_longbetadecays():
    fig, ax = plib.set_plot_style()

    R = np.logspace(-1, 3, 1000)
    
    plot_decay(ax, 4, 10, R, 1.51 * Myr, r'$\beta^-$(1.51 Myr) : $^{10}$Be $\rightarrow$ $^{10}$B', 'tab:blue')
    plot_decay(ax, 6, 14, R, 5.7 * kyr, r'$\beta^-$(5.7 kyr) : $^{14}$C $\rightarrow$ $^{14}$N', 'tab:orange')
    plot_decay(ax, 11, 22, R, 4.8 * Myr, r'$\beta^+$(4.8 Myr) : $^{22}$Na $\rightarrow$ $^{22}$Ne', 'tab:pink')
    plot_decay(ax, 13, 26, R, 0.91 * Myr, r'$\beta^+$(0.91 Myr) : $^{26}$Al $\rightarrow$ $^{26}$Mg', 'tab:green')
    plot_decay(ax, 17, 36, R, 0.307 * Myr, r'$\beta^-$(0.307 Myr) : $^{36}$Cl $\rightarrow$ $^{36}$Ar', 'tab:red')
    plot_decay(ax, 25, 54, R, 0.63 * Myr, r'$\beta^+$(0.63 Myr) : $^{54}$Mn $\rightarrow$ $^{54}$Fe', 'tab:brown')
    plot_decay(ax, 28, 56, R, 0.051 * Myr, r'$\beta^+$(51 kyr) : $^{56}$Ni $\rightarrow$ $^{56}$Fe', 'tab:olive')
    plot_decay(ax, 26, 60, R, 2.6 * Myr, r'$\beta^-$(2.6 Myr) : $^{60}$Fe $\rightarrow$ $^{60}$Co $\rightarrow$ $^{60}$Ni', 'tab:cyan')

    ax.legend(fontsize=14)

    tdiff = 5. / (1e-5 + 1e-5 * np.power(R, 0.54)) # [kyr]
    ax.plot(R, tdiff, color='k')
    ax.fill_between(R, 2. / 5.  * tdiff, 10. / 5.  * tdiff, facecolor='k', alpha=0.3, zorder=1)

    ax.set_yscale('log')
    ax.set_xscale('log')

    ax.set_xlabel(r'R [GV]')
    ax.set_ylabel('t [kyr]')
    
    #ax.plot([1, 1e3], [1, 1], ':', color='k')

    ax.set_xlim([1e0, 1e3])
    ax.set_ylim([1e-1, 1e8])
    
    plt.savefig('longbetadecays.pdf')

def plot_ghostdecays():
    fig, ax = plib.set_plot_style()
    
    filename = '../data/ghost_list.txt'
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines[1:]:
        line = line.split()
        Zp = plib.str_to_Z(line[0])
        Ap = int(line[1])
        Zd = plib.str_to_Z(line[2])
        Ad = int(line[3])
        #ax.plot([Zp, Zd], [Ap, Ad])

        rect = patches.Rectangle((Zp,Ap),1,1,linewidth=0,edgecolor='tab:gray',facecolor='tab:gray',alpha=0.3)
        ax.add_patch(rect)
        
        if (Zd - Zp) > 0:
            ax.arrow(Zp + 0.5, Ap + 0.5, (Zd - Zp) * 0.8, (Ad - Ap) * 0.8, length_includes_head=True,
                     head_width=0.3, head_length=0.2, fc='tab:orange', ec='tab:orange')
        else:
            ax.arrow(Zp + 0.5, Ap + 0.5, (Zd - Zp) * 0.8, (Ad - Ap) * 0.8, length_includes_head=True,
                    head_width=0.3, head_length=0.2, fc='tab:green', ec='tab:green')

    filename = '../data/crchart_Z28_2020.txt'
    f = open(filename, "r")
    lines = f.readlines()
    for line in lines[1:]:
        line = line.split()
        Z = int(line[0])
        A = int(line[1])
        mode = line[3]
        if (mode == 'BETA+'):
            rect = patches.Rectangle((Z,A),1,1,linewidth=0,edgecolor='tab:purple',facecolor='tab:purple',alpha=0.7)
            ax.add_patch(rect)
        elif (mode == 'BETA-'):
            rect = patches.Rectangle((Z,A),1,1,linewidth=0,edgecolor='tab:red',facecolor='tab:red',alpha=0.7)
            ax.add_patch(rect)
        else:
            rect = patches.Rectangle((Z,A),1,1,linewidth=0,edgecolor='tab:blue',facecolor='tab:blue',alpha=0.7)
            ax.add_patch(rect)
            
    ax.text(12, 12, r'409 ghost nuclei', fontsize=20)
    ax.text(12,  7, r'with msec $< \tau_{1/2} <$ kyr', fontsize=20)

    ax.text(4, 70, r'$\beta+$ ghost', color='tab:green', fontsize=18)
    ax.text(4, 65, r'$\beta-$ ghost', color='tab:orange', fontsize=18)
    ax.text(4, 60, r'$\beta+$ long-lived', color='tab:purple', fontsize=18)
    ax.text(4, 55, r'$\beta-$ long-lived', color='tab:red', fontsize=18)
    ax.text(4, 50, r'Stable', color='tab:blue', fontsize=18)

    ax.set_xlim([0, 32])
    ax.set_ylim([0, 80])
    ax.set_xlabel('Z')
    ax.set_ylabel('A')
    plt.savefig('ghostdecays.pdf')

def plot_fragments():
    fig, ax = plt.subplots(figsize=(11, 12), subplot_kw=dict(aspect="equal"))

    filename = '../crxsecs_fragmentation_Evoli2019_direct.txt'
    f = open(filename, "r")
    lines = f.readlines()
    E = lines[0]
    E = E.split()
    print (E[100])
    for line in lines[1:]:
        line = line.split()
        Zd = int(line[0])
        Ad = int(line[1])
        Zp = int(line[2])
        Ap = int(line[3])
        if (Zp == 8 and Ap == 16):
            print (Zd, Ad, line[100])

    kwargs = dict(size=50, fontweight='bold', va='center')

    recipe = ["He3", "He4", "Li6", "Li7", "Be7", "Be9", "Be10", "B10", "B11"]
    data = [3.870e+01, 1.261e+02, 1.489e+01, 1.374e+01, 9.463e+00, 7.028e+00, 3.997e+00, 1.588e+01, 2.682e+01]
    plotname = "C12_fragment.pdf"
    ax.text(0, 0, r'C$^{12}$', ha='center', **kwargs)

#    recipe = ["He3", "He4", "Li6", "Li7", "Be7", "Be9", "Be10", "B10", "B11", "C12", "C13"]
#    data = [9.648e+00,1.271e+01,1.260e+01,1.138e+01,1.210e+01,2.536e+00,2.638e+00,9.686e+00,1.642e+01,5.131e+01,7.957e+00]
#    plotname = "N14_fragment.pdf"
#    ax.text(0, 0, r'N$^{14}$', ha='center', **kwargs)

#    recipe = ["He3", "He4", "Li6", "Li7", "Be7", "Be9", "Be10", "B10", "B11", "C12", "C13", "C14", "N14", "N15"]
#    data = [5.012e+01,1.261e+02,1.601e+01,1.083e+01,8.690e+00,3.213e+00,3.954e+00,9.144e+00,1.580e+01,3.148e+01,1.657e+01,1.756e+00,2.929e+01,3.232e+01]
#    plotname = "O16_fragment.pdf"
#    ax.text(0, 0, r'O$^{16}$', ha='center', **kwargs)
 
    wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)

    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
              bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.5*y), fontsize=18, horizontalalignment=horizontalalignment, **kw)

    plt.savefig(plotname)

#plot_longbetadecays()
#plot_betadecays('../../data/betadecays_list.txt')

#plot_ghostdecays()
plot_fragments()
