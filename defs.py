
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