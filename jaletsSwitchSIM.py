# Samuel Rivera
# Jan 20, 2016
# This script is meant for generating switch flurps/jalets

from PIL import Image, ImageDraw
from collections import OrderedDict
import os
from jalets import *

      
if __name__ == '__main__':

    # make output folder
    outFolder=  'FlurpJaletSwitchSIM/'
    if not os.path.exists( outFolder):
        os.mkdir( outFolder)
        

    # make jalet object 
    j = JaletSIM( )

    # get list of all Jalet structures, then draw and save
    trueBase = 0
    switchBase = 1
    switchOut = 0
    allProbList = getProbStruct( nProb = 6, baseVal=switchBase, outVal=switchOut)
    for struct in allProbList:
        struct[0] = trueBase
        jaletImg = j.draw(struct)
        name = outFolder + 'J_SW_' + ''.join(str(x) for x in struct) + '_SIM.png'
        print( name)
        jaletImg.save( name )

    # get list of all Flurp structures, then draw and save
    trueBase = 1
    switchBase = 0
    switchOut = 1
    allProbList = getProbStruct( nProb = 6, baseVal=switchBase, outVal=switchOut)
    for struct in allProbList:
        struct[0] = trueBase
        jaletImg = j.draw(struct)
        name = outFolder + 'F_SW_' + ''.join(str(x) for x in struct) + '_SIM.png'
        print( name)
        jaletImg.save( name )


