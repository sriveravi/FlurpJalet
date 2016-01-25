# Samuel Rivera
# Jan 20, 2016
# This script is meant for generating flurps/jalets with the redundent features

from PIL import Image, ImageDraw
from collections import OrderedDict
import os

from jalets import *


if __name__ == '__main__':

    # make output folder
    outFolder=  'FlurpJaletSIM/'
    if not os.path.exists( outFolder):
        os.mkdir( outFolder)
        

    # make jalet object 
    j = JaletSIM( )

    # get list of all Jalet structures, then draw and save
    allProbList = getProbStruct( nProb = 6, baseVal=0, outVal=1)
    for struct in allProbList:
        jaletImg = j.draw(struct)
        name = outFolder + 'J_' + ''.join(str(x) for x in struct) + '_SIM.png'
        print( name)
        jaletImg.save( name )

    # get list of all Flurp structures, then draw and save
    allProbList = getProbStruct( nProb = 6, baseVal=1, outVal=0)
    for struct in allProbList:
        jaletImg = j.draw(struct)
        name = outFolder + 'F_' + ''.join(str(x) for x in struct) + '_SIM.png'
        print( name)
        jaletImg.save( name )
