#Monomials
#Gauge Monomials
#Fermion Monomials
params={}
params['Monomials']={}

params['Monomials']['GAUGE_MONOMIAL']={'ACTION':'WILSON_GAUGEACT',
                                      'BETA':'8.4','ID':'HMC::gauge'}
params['Monomials']['ONE_FLAVOR_EOPREC']={'ACTION':'CLOVER',
                                          'MASS':'-0.5','CLOV_COEFF':'1.12','ID':'HMC::strange'}
params['Monomials']['TWO_FLAVOR_EOPREC']={'ACTION':'CLOVER','MASS':'-0.5',
                                          'CLOV_COEFF':'1.12','ID':'HMC::light'}

params['Monomial_ids']=''

for m in params['Monomials'].keys():
    if 'TWO_FLAVOR_EOPREC' in m:
      params['Monomial_ids']+='\t\t\t\t\t<elem>'+params['Monomials'][m]['ID']+'_ee</elem>\n'
      params['Monomial_ids']+='\t\t\t\t\t<elem>'+params['Monomials'][m]['ID']+'_oo</elem>\n'
    else:
      params['Monomial_ids']+='\t\t\t\t\t<elem>'+params['Monomials'][m]['ID']+'</elem>\n'

#MD integrator
#Choose the integrator parameters
params['integrator']={'NAME':'LCM_STS_LEAPFROG','NSTEPS':'64'}
params.update(params['integrator'])
#HMC updates
params['WARMUPS']='1'
params['PROD_UPDATES']='1'
params['NUPDATES']='1'
monomials=''
for m in params['Monomials'].keys():
  monomials+=xml_input.monomials[m]%params['Monomials'][m]
integrator=params['integrator']['NAME']

params.update({'VOL':' 4 4 4 16','CFG':'DISORDERED','TAU':'0.05',
        'MONOMIALS':monomials,'MONOMIAL_IDS':params['Monomial_ids']})