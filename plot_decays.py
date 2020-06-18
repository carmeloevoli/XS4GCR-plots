import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np
import math

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

def plot_betadecays(filename):
    fig, ax = plib.set_plot_style()
    Z, A, tau = read_ghosts(filename)
    ax.set_yscale('log')
    ax.plot(Z, tau, 'o')
    ax.plot([0, 30], [kyr, kyr], ':')
    plt.savefig('betadecays.pdf')

#plot_longbetadecays()
#plot_betadecays('../../data/betadecays_list.txt')
