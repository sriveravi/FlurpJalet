# Samuel Rivera
# Jan 20, 2016
# This script/module is meant for generating flurps/jalets

from PIL import Image, ImageDraw
from collections import OrderedDict
import os




class Jalet:
    def __init__( self, partsDict = None, positions= None  ):

        if partsDict == None:
            partsDict = OrderedDict()
            partsDict[ 'tailBone'] = ['Parts/tailBone.png', 'Parts/tailBone.png']
            partsDict[ 'head'] = ['Parts/head0.png', 'Parts/head1.png', 'Parts/coverSmall.png']
            partsDict[ 'body'] = ['Parts/body0.png', 'Parts/body1.png', 'Parts/coverBig.png']
            partsDict[ 'button'] = ['Parts/but0.png','Parts/but1.png', 'Parts/coverSmall.png']
            partsDict[ 'lEye'] = ['Parts/lEye0.png', 'Parts/lEye1.png']
            partsDict[ 'rEye'] = ['Parts/rEye0.png', 'Parts/rEye1.png']
            partsDict[ 'lHand'] = ['Parts/lHand0.png', 'Parts/lHand1.png', 'Parts/coverSmall.png']
            partsDict[ 'rHand'] = ['Parts/rHand0.png', 'Parts/rHand1.png', 'Parts/coverSmall.png']
            partsDict[ 'lAntenna'] = ['Parts/lAnt0.png', 'Parts/lAnt1.png', 'Parts/coverSmall.png']
            partsDict[ 'rAntenna'] = ['Parts/rAnt0.png', 'Parts/rAnt1.png', 'Parts/coverSmall.png']
            partsDict[ 'lFoot'] = ['Parts/lFoot0.png', 'Parts/lFoot1.png', 'Parts/coverSmall.png']
            partsDict[ 'rFoot'] = ['Parts/rFoot0.png', 'Parts/rFoot1.png', 'Parts/coverSmall.png']
            partsDict[ 'tail'] = ['Parts/tail0.png', 'Parts/tail1.png', 'Parts/coverSmall.png']

        if positions == None:
            positions = { 'head': (0,-170),
                'body':(0,80),
                'lFoot':(-70, 360),
                'rFoot':(70, 360),
                'tail':(-270, 210),
                'lEye':(-25,-150),
                'rEye':(25,-150),
                'lHand': (-200,0),
                'rHand': (200,0),
                'button':(0,80),
                'lAntenna':(-120,-350),
                'rAntenna':(120,-350),
                'tailBone':(-160,170)}
        # initialize  things:
        self.imSize = (700,900)  # x,y
        self.partsDict = partsDict
        self.pos = positions

    def draw( self, indices = [0,0,0,0,0,0,0]):
        # return drawn image of given category structure
        #
        # labIdxDict tells where in the indices vector will have that feature
        # typically it is going to be a 0 or 1
        labIdxDict = { 'head': 1,
            'body': 2 ,
            'lFoot':4,
            'rFoot':4,
            'tail':6,
            'lEye':0,
            'rEye':0,
            'lHand':3,
            'rHand':3,
            'button': 0,
            'lAntenna':5,
            'rAntenna':5,
            'tailBone':0}

        # make bg for drawing
        self.image = Image.new( 'RGBA', self.imSize, (255,255,255,0)) # last int for transpernt, make 0
        center = tuple([x/2 for x in self.imSize])  

        # draw the lines
        draw = ImageDraw.Draw(self.image) 
	draw.line( [ addCoords(center,self.pos['body']), addCoords(center,self.pos['head'])], fill=(0,0,0),width=4)
	draw.line( [ addCoords(center,self.pos['lAntenna']), addCoords(center,self.pos['head'])], fill=(0,0,0),width=4)
	draw.line( [ addCoords(center,self.pos['rAntenna']), addCoords(center,self.pos['head'])], fill=(0,0,0),width=4)
	draw.line( [ addCoords(center,self.pos['body']), addCoords(center,self.pos['lFoot'])], fill=(0,0,0),width=4)
	draw.line( [ addCoords(center,self.pos['body']), addCoords(center,self.pos['rFoot'])], fill=(0,0,0),width=4)
	draw.line( [ addCoords(center,self.pos['body']), addCoords(center,self.pos['lHand'])], fill=(0,0,0),width=4)
	draw.line( [ addCoords(center,self.pos['body']), addCoords(center,self.pos['rHand'])], fill=(0,0,0),width=4)

        # draw all parts where they go
        for partName in self.partsDict.keys():      #self.parts.items():
            partIdx =indices[ labIdxDict[partName]]
            part = Image.open( self.partsDict[partName][partIdx] ) # part image
            partPos = addCoords( center, self.pos[partName])
            # add part to background
            self.image.paste( part, centerPos(partPos,part.size), mask=part)

        # return the drawn image
        return self.image
        # show it
        #newSize = tuple([ x/2 for x in self.imSize])  
        #smallImg = self.image.resize( newSize) #, Image.LINEAR)
        #smallImg.show()
        #self.image.show()



def getProbStruct( nProb = 6, baseVal=0, outVal=1):
    # return list of lists of the structure (like ones/zeros)
    allStructs = []
    for i1 in range(nProb):
        for i2 in range(i1+1,nProb):
            featIdxList = [baseVal]*(nProb)
            featIdxList[i1] = outVal
            featIdxList[i2] = outVal
            allStructs.append([baseVal] +featIdxList)
    return allStructs

# general methods for shifting around coordinates
# because I do it several times
def addCoords( pos1, pos2 ):
    # add up the two coordinates in a tuple, return a tuple 
    return (pos1[0]+pos2[0], pos1[1]+pos2[1])       

def centerPos( targetPos, imSize ):
    # get top-left coordinate for an image if it is
    # to be centered at a particular coordinate
    return (targetPos[0]-imSize[0]/2, targetPos[1]-imSize[1]/2)


#==============================================================
#==============================================================

if __name__ == '__main__':

    # make output folder
    outFolder=  'FlurpJaletStd/'
    if not os.path.exists( outFolder):
        os.mkdir( outFolder)
        

    # make jalet object 
    j = Jalet( )

    # get list of all Jalet structures, then draw and save
    allProbList = getProbStruct( nProb = 6, baseVal=0, outVal=1)
    for struct in allProbList:
        jaletImg = j.draw(struct)
        name = outFolder + 'J' + ''.join(str(x) for x in struct) + '.png'
        print( name)
        jaletImg.save( name )

    # get list of all Flurp structures, then draw and save
    allProbList = getProbStruct( nProb = 6, baseVal=1, outVal=0)
    for struct in allProbList:
        jaletImg = j.draw(struct)
        name = outFolder + 'F' + ''.join(str(x) for x in struct) + '.png'
        print( name)
        jaletImg.save( name )


