import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import numpy as np
import math

import plot_lib as plib

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

def find_isotope(Z, A, Zp, Ap):
    foundit = False
    for Zp_, Ap_ in zip(Zp, Ap):
        if Zp_ == Z and Ap_ == A:
            foundit = True
    return foundit
    
def check_decays(filename):
    Zp, Ap, tau = read_ghosts(filename)
    Zs, As = np.loadtxt('../../data/crchart_Z28.txt', skiprows=1, usecols=(0,1), unpack=True)
    
    Zc, Ac = read_child(filename)
    for Z,A in zip(Zc, Ac):
        if (find_isotope(Z, A, Zs, As)):
            print ('Child ', Z, A, 'is stable!')
        elif (find_isotope(Z, A, Zp, Ap)):
            print ('Child ', Z, A, 'is a known decaying particle')
        else:
            print ('Child ', Z, A, 'has an unknown doom')

def check_isGhost(filename):
    Zp, Ap, tau = read_ghosts('../../data/betadecays_list.txt')
    
    ZU, AU = np.loadtxt(filename, skiprows=0, usecols=(0,1), unpack=True)
    for Z,A in zip(ZU, AU):
        if not find_isotope(Z, A, Zp, Ap):
            print (int(Z), int(A), 'What is this?')
        #else:
        #    print (int(Z), int(A), 'Is ghost!')

#plot_longbetadecays()
#plot_betadecays('../../data/betadecays_list.txt')

#check_decays('../../data/betadecays_list.txt')

check_isGhost('USINE_ghostlist.txt')
