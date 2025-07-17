import numpy as np
import gvar as gv
import h5py as h5
import random
from process_correlators import *
from fit_params import *
from fit_priors import *



#Fits two correlators
def c2pt(x, p):       #function used to fit x, y data
	nt=x.shape[0]
	temp=np.zeros(shape=(nt))
	result=gv.gvar(temp,temp)
	a0,a1=p['a0'],p['a1']
	E=[gv.fabs(e) for e in p['E']]
	E0=E[0]
	E[0]=0.0
	result[0:nt/2]=sum(ai * np.exp(-(E0+Ei) * x[0:nt/2]) for ai, Ei in zip(a0, E))
	result[nt/2:nt]=sum(ai * np.exp(-(E0+Ei) * x[0:nt/2]) for ai, Ei in zip(a1, E))
	return result

#Fits two correlators
def fcn(x, p):       #function used to fit x, y data
	nt=x.shape[0]
	temp=np.zeros(shape=(nt))
	result=gv.gvar(temp,temp)
	a0,a1=p['A0'],p['A1']
	E=[gv.fabs(e) for e in p['E']]
	E0=E[0]
	E[0]=0.0
	result=sum(ai * np.exp(-(E0+Ei) * x) for ai, Ei in zip(a0, E))
	return result

def make_fh_ratio(corr,fh_corr):
	corr_fh_p1=np.roll(fh_corr,-1,axis=1)
	corr_p1=np.roll(corr,-1,axis=1)
	return fh_corr/corr-corr_fh_p1/corr_p1


def make_prior(nexp):               # make priors for fit parameters
    prior = gv.BufferDict()         # any dictionary works
    prior['A0'] = [gv.gvar(0.5, 0.4) for i in range(nexp)]
    prior['A1'] = [gv.gvar(0.5, 0.4) for i in range(nexp)]
    prior['E'] = [gv.gvar(i+1, 0.4) for i in range(nexp)]
    return prior

'''
def make_prior(nexp,ens,particle):               # make priors for fit parameters
    prior = gv.BufferDict()         # any dictionary works
    A0List,EList=dicParametros[ens][particle]['A0'],dicParametros[ens][particle]['E']
    A1List=dicParametros[ens][particle]['A1']
    prior['A0'] = [gv.gvar(A0List[i], 0.4) for i in range(nexp)]
    prior['A1'] = [gv.gvar(A1List[i], 0.4) for i in range(nexp)]
    prior['E'] = [gv.gvar(EList[i], 0.4) for i in range(nexp)]
    return prior
''' 
