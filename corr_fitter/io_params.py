import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter,FuncFormatter

##################PLOT DEFAULTS###############################
rcParams={'text.latex.preamble':r'\usepackage{amsmath} \usepackage{amssymb} \usepackage{slashed}',
          'text.usetex':False}
        
plt_rcParam={'axes.linewidth':2.5, 'font.size':25, 'font.weight':1000,'legend.fontsize':25,
             'legend.markerscale':1.5,'grid.linewidth':1.5,'lines.linewidth':2.5,'axes.labelsize':30}
matplotlib.rcParams.update(rcParams)
plt.rcParams.update(plt_rcParam)

figS=(12,7.5)
marker='o'
ms=10.
mew=3.5
capsize=4
legTextSize=25
mycolors= ['k', 'b', 'r', 'g', 'y', 'm', 'c']
##################PLOT DEFAULTS###############################


