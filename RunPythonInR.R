library(reticulate)

reticulate::repl_python()
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
t = np.arange(0.0,2,0.01)
s = 1 + np.sin(2*np.pi*t)



os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:/Users/sconroy/AppData/Local/Continuum/anaconda3/Library/plugins/platforms'
plt.plot(t,s)
plt.show()

t
S = pd.Series([1,3,4,np.nan,6,8])
print(S)
exit  # switch back to R

# Access Python Objects back in R
reticulate::py$S
