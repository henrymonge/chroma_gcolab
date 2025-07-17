import os,sys
from io_params import *
import numpy as np
import gvar as gv
import h5py as h5
from fit_functions import *
import lsqfit


plt.ion()

f=h5.File('../a09m260_a_avg_srcs0-7.h5')
particle='proton'  #kplus,lambda_z,omega_m,piplus,proton
isMeson=particle in ['pion','kminus','kplus','piplus']

path='gf1p0_w3p5_n45_M51p1_L58_a1p5/spec/ml0p00702_ms0p0481'
#Retrieve data
if isMeson:
    corr=f[path+f'/{particle}/psq_0/corr'][()].real
else:
    corr_spin_dn=f[path+f'/{particle}/psq_0/spin_dn'][()].real
    corr_spin_up=f[path+f'/{particle}/psq_0/spin_up'][()].real
    corr=(corr_spin_dn+corr_spin_up)  #spin average
corr=corr[:,:,1,0]

#time extent
T=corr.shape[1]

#Pack the mean and std into a gvar
j=1
x=np.arange(T)
y=gv.dataset.avg_data(corr)
y_pj = np.roll(y,-j)
y_mj = np.roll(y,j)

#Compute the meff
if isMeson:
    meff =  1. / j * np.arccosh((y_pj+y_mj) / 2 / y )
else:
    meff =  1. / j * np.log( y / y_pj )

#Plot correlator
fig = plt.figure(1,figsize=(20,10))
ax=plt.subplot()
ax.errorbar(np.arange(T),gv.mean(y), yerr=gv.sdev(y),ms=ms,mew=mew,
                mfc='None',capsize=capsize,linestyle='None',alpha=0.9)
ax.set_xlabel('$t$')
ax.set_ylabel('$C(t)$')
plt.title(particle)
plt.show(block=False)

#Plot meff
fig = plt.figure(2,figsize=(20,10))
ax=plt.subplot()
ax.errorbar(np.arange(T),gv.mean(meff), yerr=gv.sdev(meff),ms=ms,mew=mew,
                mfc='None',capsize=capsize,linestyle='None',alpha=0.9)
ax.set_xlabel('$t$')
ax.set_ylabel('$m_{eff}$')
plt.title(particle)
plt.show()

p0 = None    # make larger fits go faster (opt.)
nstates=1
for nexp in range(1, nstates+1):
	print('************************************* nexp =', nexp)
	prior = make_prior(nexp)
	fit = lsqfit.nonlinear_fit(data=(x, y), fcn=fcn, prior=prior,p0=p0)
	print(fit)		  # print the fit results

	if nexp > 2:
		E = fit.p['E']	  # best-fit parameters
		a = fit.p['a0']
		print('E1/E0 =', E[1] / E[0], '  E2/E0 =', E[2] / E[0])
		print('a1/a0 =', a[1] / a[0], '  a2/a0 =', a[2] / a[0])
		if fit.chi2 / fit.dof < 1.:
			p0 = fit.pmean	  # starting point for next fit (opt.)
		print()

		# error budget analysis
		outputs = {	'E1/E0':E[1]/E[0], 'E2/E0':E[2]/E[0],
    	            'a1/a0':a[1]/a[0], 'a2/a0':a[2]/a[0]}
                
		inputs = {'E':fit.prior['E'], 'a0':fit.prior['a0'],'a1':fit.prior['a1'], 'y':y}
		print('================= Error Budget Analysis')
		print(fit.fmt_values(outputs))
		print(fit.fmt_errorbudget(outputs,inputs))

#posterior fit.p['E']
#meff_fit=fit.p['E'][0]
#ax.fill_between(x,meff_fit.mean-meff_fit.sdev, meff_fit.mean+meff_fit.sdev,facecolor='k',alpha=0.25)

plt.ioff()
