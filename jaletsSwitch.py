# Samuel Rivera
# Jan 20, 2016
# This script is meant for generating switch flurps/jalets

from PIL import Image, ImageDraw
from collections import OrderedDict
import os
from jalets import *

      
if __name__ == '__main__':

    # make output folder
    outFolder=  'FlurpJaletSwitch/'
    if not os.path.exists( outFolder):
        os.mkdir( outFolder)
        

    # make jalet object 
    j = Jalet( )

    # get list of all Jalet structures, then draw and save
    trueBase = 0
    switchBase = 1
    switchOut = 0
    allProbList = getProbStruct( nProb = 6, baseVal=switchBase, outVal=switchOut)
    for struct in allProbList:
        struct[0] = trueBase
        jaletImg = j.draw(struct)
        name = outFolder + 'J' + ''.join(str(x) for x in struct) + '.png'
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
        name = outFolder + 'F' + ''.join(str(x) for x in struct) + '.png'
        print( name)
        jaletImg.save( name )


