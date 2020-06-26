import numpy as np
import math
import plot_lib as plib

def find_isotope(Z, A, Zp, Ap):
    foundit = False
    for Zp_, Ap_ in zip(Zp, Ap):
        if Zp_ == Z and Ap_ == A:
            foundit = True
    return foundit
    
def check_decays(filename):
    Zp, Ap, tau = plib.read_ghosts(filename)
    Zs, As = np.loadtxt('../../data/crchart_Z28.txt', skiprows=1, usecols=(0,1), unpack=True)
    
    Zc, Ac = plib.read_child(filename)
    for Z,A in zip(Zc, Ac):
        if (find_isotope(Z, A, Zs, As)):
            print ('Child ', Z, A, 'is stable!')
        elif (find_isotope(Z, A, Zp, Ap)):
            print ('Child ', Z, A, 'is a known decaying particle')
        else:
            print ('Child ', Z, A, 'has an unknown doom')

def check_isGhost(filename):
    Zp, Ap, tau = plib.read_ghosts('../../data/betadecays_list.txt')
    
    ZU, AU = np.loadtxt(filename, skiprows=0, usecols=(0,1), unpack=True)
    for Z,A in zip(ZU, AU):
        if not find_isotope(Z, A, Zp, Ap):
            print (int(Z), int(A), 'What is this?')
        #else:
        #    print (int(Z), int(A), 'Is ghost!')

def check_duplicate():
    Zp, Ap, tau = plib.read_ghosts('../../data/ghost_list.txt')
    Zs, As = np.loadtxt('../../data/crchart_Z28_2020.txt', skiprows=1, usecols=(0,1), unpack=True)
    
    for Z,A in zip(Zs,As):
        if find_isotope(Z, A, Zp, Ap):
            print (int(Z), int(A))

#check_decays('../../data/betadecays_list.txt')
#check_isGhost('USINE_ghostlist.txt')
check_duplicate()
