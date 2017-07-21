import math

class Grid:
    
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.nodeConstant = 3
        self.midpoint = [0.5*(x2+x1),0.5*(y2-y1)]

    def maxNode(self,pointList):
        count = 0
        for point in pointList:
            xvalue,yvalue = point.getPosition()[0],point.getPosition()[1]
            if self.x1 <= xvalue <= self.x2 or self.x2 <= xvalue <= self.x1:
                x = True
            else:
                x = False
            if self.y1 <= yvalue <= self.y2 or self.y2 <= yvalue <= self.y1:
                y = True
            else:
                y = False
            if x == True and y == True:
                radius = 0.5*(math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2))
                point.setRadius(radius)
                count = count + 1
        if count > self.nodeConstant:
            return 'TurnUp'
        elif count <= self.nodeConstant:
            return 'TurnDown'
        
            
                
