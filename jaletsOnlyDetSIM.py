# Samuel Rivera
# Jan 20, 2016
# This script/module is meant for generating flurps/jalets with
# only deterministic button feature (all others covered)

from PIL import Image, ImageDraw
from collections import OrderedDict
import os
from jalets import *

#==============================================================
#==============================================================

if __name__ == '__main__':

    # make output folder
    outFolder=  'FlurpJaletOnlyDetSIM/'
    if not os.path.exists( outFolder):
        os.mkdir( outFolder)
        

    # make jalet object, remove the button part from description
    j = JaletSIM( )

    # get list of all Jalet structures, then draw and save
    # allProbList = getProbStruct( nProb = 6, baseVal=0, outVal=1)
    for i1 in range(5):
        struct = [0,2,2,2,2,2,2] 
        jaletImg = j.draw(struct)
        struct[1:] = '?'*6
        name = outFolder + 'J_DE_' + ''.join(str(x) for x in struct) + '_' + str(i1) + '_SIM.png'
        print( name)
        jaletImg.save( name )

    # get list of all Flurp structures, then draw and save
    #allProbList = getProbStruct( nProb = 6, baseVal=1, outVal=0)
    for i1 in range(5):
        struct = [1,2,2,2,2,2,2] 
        jaletImg = j.draw(struct)
        struct[1:] = '?'*6
        name = outFolder + 'F_DE_' + ''.join(str(x) for x in struct) + '_' + str(i1) +  '_SIM.png'
        print( name)
        jaletImg.save( name )


