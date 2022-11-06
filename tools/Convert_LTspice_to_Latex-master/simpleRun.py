import os
import sys

from LTspiceToTexConverter import *

if os.name == 'nt':
    path_ltspice = r'C:\Program Files\LTC\LTspiceXVII\lib\sym'
else:
    path_ltspice = sys.argv[1]

fileName_input = sys.argv[2]

out = LtSpiceToLatex(filenameLTspice=fileName_input,
                     lt_spice_directory=os.path.expanduser(path_ltspice),
                     fullExample=0)

print(out)
