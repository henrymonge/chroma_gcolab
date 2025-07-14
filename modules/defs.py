import numpy as np
import xml_input 
monomial_tex={'GAUGE_MONOMIAL':
'\\frac12\\textrm{Tr}\\: F_{\\mu\\nu}F^{\\mu\\nu}'}
monomial_tex['TWO_FLAVOR_EOPREC']='\\sum_{f=1}^2\\bar\\psi_f (i \\gamma^\\mu \\partial_\\mu - m_f)'
monomial_tex['TWO_FLAVOR_EOPREC']+= '\\psi_f  - g \\sum_{f=1}^2 A_\\mu^a \\bar\\psi_f \\gamma^\\mu \\lambda_a \\psi_f'
monomial_tex['ONE_FLAVOR_EOPREC']='\\bar\\psi_f (i \\gamma^\\mu \\partial_\\mu - m_f) \\psi_f  - g A_\\mu^a'
monomial_tex['ONE_FLAVOR_EOPREC']+='\\bar\\psi_f \\gamma^\\mu\\lambda_a \\psi_f'


def display_action(my_monomials):
  from IPython.display import display, Latex
  print('\n\n'+'*'*50)
  print(' '*15+'My chosen action is:')
  print('*'*50+'\n')

  from IPython.display import display, Latex

  my_action='$\\mathcal{S}_\\text{QCD}='
  for m in my_monomials.keys():
    my_action+='\\large\\int'+monomial_tex[m]+'+'
  my_action=my_action[:-1]

  display(Latex(my_action+'$'))

def getVolumeSites(params):
    vol=params['VOL'].split(' ')[-4::]
    vol=np.array([int(i) for i in vol])
    return vol.prod()

def writeInputFile(params,outdir):
  base_xml='/home/tests/template_hmc.ini.xml.txt'
  ini=outdir+'/hmc.ini.xml'
  out=outdir+'/hmc.out'
  log=outdir+'/hmc.log'
  stdout=outdir+'/hmc.stdout'
  fin=open(base_xml)
  fout=open(ini,'w')
  fout.write(fin.read()%params)
  fin.close()
  fout.close()

  return ini,out,log,stdout

def writeInputFileProp(params,outdir):
  base_xml='/home/tests/template_prop.ini.xml.txt'
  ini=outdir+'/prop.ini.xml'
  out=outdir+'/prop.out'
  log=outdir+'/prop.log'
  stdout=outdir+'/prop.stdout'
  fin=open(base_xml)
  fout=open(ini,'w')
  fout.write(fin.read()%params)
  fin.close()
  fout.close()

  return ini,out,log,stdout

def writeInputFileHadspec(params,outdir):
  base_xml='/home/tests/template_hadspec.ini.xml.txt'
  ini=outdir+'/hadspec.ini.xml'
  out=outdir+'/hadspec.out'
  log=outdir+'/hadspec.log'
  stdout=outdir+'/hadspec.stdout'
  fin=open(base_xml)
  fout=open(ini,'w')
  fout.write(fin.read()%params)
  fin.close()
  fout.close()

  return ini,out,log,stdout

def setMonomialIds(params):
  params['Monomial_ids']=''
  for m in params['Monomials'].keys():
      if 'TWO_FLAVOR_EOPREC' in m:
        params['Monomial_ids']+='\t\t\t\t\t<elem>'+params['Monomials'][m]['ID']+'_ee</elem>\n'
        params['Monomial_ids']+='\t\t\t\t\t<elem>'+params['Monomials'][m]['ID']+'_oo</elem>\n'
      else:
        params['Monomial_ids']+='\t\t\t\t\t<elem>'+params['Monomials'][m]['ID']+'</elem>\n'
  
  monomials=''
  for m in params['Monomials'].keys():
    monomials+=xml_input.monomials[m]%params['Monomials'][m]
  params['MONOMIALS']=monomials
  params['MONOMIAL_IDS']=params['Monomial_ids']
