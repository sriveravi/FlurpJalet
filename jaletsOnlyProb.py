# Samuel Rivera
# Jan 20, 2016
# This script/module is meant for generating flurps/jalets without
# the deterministic button feature

from PIL import Image, ImageDraw
from collections import OrderedDict
import os
from jalets import *

#==============================================================
#==============================================================

if __name__ == '__main__':

    # make output folder
    outFolder=  'FlurpJaletOnlyProb/'
    if not os.path.exists( outFolder):
        os.mkdir( outFolder)
        

    # make jalet object, remove the button part from description
    j = Jalet( )
    j.partsDict.pop('button')

    # get list of all Jalet structures, then draw and save
    allProbList = getProbStruct( nProb = 6, baseVal=0, outVal=1)
    for struct in allProbList:
        jaletImg = j.draw(struct)
        struct[0] = '?'
        name = outFolder + 'J' + ''.join(str(x) for x in struct) + '.png'
        print( name)
        jaletImg.save( name )

    # get list of all Flurp structures, then draw and save
    allProbList = getProbStruct( nProb = 6, baseVal=1, outVal=0)
    for struct in allProbList:
        jaletImg = j.draw(struct)
        struct[0] = '?'
        name = outFolder + 'F' + ''.join(str(x) for x in struct) + '.png'
        print( name)
        jaletImg.save( name )


