
import os
import sys
sys.path.append(os.path.dirname(__file__))
from tools import *

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "DGAAE"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [Equiv,Act_Equiv,Estandariza_cenfemul,Coord,CAT_LOC,SIIPSO,Pre_SEDESOL]
