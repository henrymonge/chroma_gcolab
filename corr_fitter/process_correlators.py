import sys
import numpy as np

"""
define colors and shapes to use in plots
"""
colors = ['k','r','g','b','y','m','c']
shapes = ['s','o','d','p','h','^','v','>','<']

'''
TIME REVERSE
'''
def time_reverse(corr,phase=1):
    ''' assumes time index is second of array '''
    NT = corr.shape[1]
    c = np.zeros_like(corr)
    c[:,0] = corr[:,0]
    for t in range(1,NT):
        c[:,t] = phase * corr[:,NT-t]
    return c

"""
Create JK list of corr
"""
def jk_corr(corr,djk=1,rescale=True):
    Ncfg = np.shape(corr)[0]
    NT = np.shape(corr)[1]
    if Ncfg % djk == 0:
        njk = Ncfg / djk
    else:
        njk = Ncfg / djk + 1
    jklst = []
    for i in range(njk-1):
        jklst.append(np.arange(i*djk,(i+1)*djk,1))
    jklst.append(np.arange((njk-1)*djk,Ncfg,1))
    jkData = []
    for jk in range(njk):
        jkData.append(np.mean(np.delete(corr,jklst[jk],axis=0),axis=0,dtype=np.float64))
    jkData = np.array(jkData)
    if rescale:
        d_jk = jkData - np.mean(jkData,axis=0)
        jkData = np.mean(jkData,axis=0) + np.sqrt(njk-1)*d_jk

    return jkData

"""
Create BS list of corr
Nbs = number of bootstraps
Mbs = number of random samplings used for each bootstrap
sig_bs * sqrt(Mbs / Ncfg) = err_mean
"""
def bs_corr(corr,Nbs,Mbs,seed=None,rescale=True):
    corr_bs = np.zeros(tuple([Nbs]) + corr.shape[1:])
    np.random.seed(seed) # if None - it does not seed - I checked 14 May 2013
    for bs in range(Nbs):
        corr_bs[bs] = corr[np.random.randint(0,corr.shape[0],Mbs)].mean(axis=0)
    if rescale:
        d_corr_bs = corr_bs - corr_bs.mean(axis=0)
        corr_bs = corr_bs.mean(axis=0) + d_corr_bs * np.sqrt(1. * Mbs / corr.shape[0])
    return corr_bs

"""
Create Effective Mass using JK loop
"""
def eff_mass(dat,j=1,type='exp',resample='jk',djk=1,Nbs=None,Mbs=None):
    if resample == 'jk':
        corr_res = jk_corr(dat,djk=djk)
    elif resample == 'bs':
        if Nbs == None:
            Nbs = dat.shape[0]
        if Mbs == None:
            Mbs = dat.shape[0]
        corr_res = bs_corr(dat,Nbs,Mbs)
    #print(corr_res.shape)
    Njk = np.shape(corr_res)[0]
    NT = np.shape(corr_res)[1]
    corr_avg = np.mean(dat,axis=0,dtype=np.float64)
    corr_avg_pj = np.roll(corr_avg,-j,axis=0)
    corr_res_pj = np.roll(corr_res,-j,axis=1)

    if type == 'exp':
        # NOTE: I have used a 'masked array [ma]' to only get sensible numbers
        # http://stackoverflow.com/questions/4485779/ignoring-inf-values-in-arrays-using-numpy-scipy-in-python
        eff = ( 1 / float(j)) * np.ma.log( corr_avg / corr_avg_pj )
        eff_jk = ( 1 / float(j)) * np.ma.log( corr_res / corr_res_pj )

    elif type == 'cosh':
        corr_avg_mj = np.roll(corr_avg,j,axis=0)
        corr_res_mj = np.roll(corr_res,j,axis=1)
        eff = ( 1 / float(j)) * np.ma.arccosh((corr_avg_pj + corr_avg_mj) / 2 / corr_avg )
        eff_jk = ( 1 / float(j)) * np.ma.arccosh((corr_res_pj + corr_res_mj) / 2 / corr_res )

    elif type == 'cosh_const' or type == 'cosh_c':
        corr_avg_p2j = np.roll(corr_avg,-2*j,axis=0)
        corr_avg_mj = np.roll(corr_avg,j,axis=0)
        corr_avg_m2j = np.roll(corr_avg,2*j,axis=0)
        corr_res_p2j = np.roll(corr_res,-2*j,axis=1)
        corr_res_mj = np.roll(corr_res,j,axis=1)
        corr_res_m2j = np.roll(corr_res,2*j,axis=1)
        corr_ratio = (corr_avg_p2j - corr_avg_m2j) / 2 / (corr_avg_pj - corr_avg_mj)
        eff = ( 1 / float(j)) * np.ma.arccosh(corr_ratio)
        eff_jk = ( 1 / float(j)) * np.ma.arccosh((corr_res_p2j - corr_res_m2j) / 2 / (corr_res_pj - corr_res_mj) )

    else:
        print("only exp and cosh and cosh_const eff mass set up so far")
        print('run again')
        sys.exit(-1)
        
    eff_jk_avg = np.ma.mean(eff_jk,axis=0,dtype=np.float64)
    eff_jk_err = np.ma.std(eff_jk - eff_jk_avg,axis=0,dtype=np.float64)
    # I add corr_avg to the return variables
    return eff, eff_jk_err, corr_avg

"""
avg correlators
"""
#def avg_corr():


