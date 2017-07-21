from Grid import *

# Adjust these values in the grid object to better suit the map of points. In the
# future we cna make this more autonomous.
#gridObject = Grid(0.0,0.0,100.0,100.0)

def Refine(gridObject, pointList):
    
    workingGridList = [gridObject]
    finalGridList = []

    #howManyNodes = workingGridList[0].maxNode(pointList)
    
    run = True
    while run :
        if len(workingGridList) == 0:
            run = False
            
        elif workingGridList[0].maxNode(pointList) == 'TurnUp':

            distanceBtweenX = abs(workingGridList[0].x1 - workingGridList[0].x2)
            distanceBtweenY = abs(workingGridList[0].y1 - workingGridList[0].y2)
            
            xMidPoint = (workingGridList[0].x1 + workingGridList[0].x2)/2.0
            yMidPoint = (workingGridList[0].y1 + workingGridList[0].y2)/2.0

            xTopRight = xMidPoint + 0.5*distanceBtweenX
            yTopRight = yMidPoint + 0.5*distanceBtweenY

            xBotRight = xMidPoint + 0.5*distanceBtweenX
            yBotRight = yMidPoint - 0.5*distanceBtweenY

            xBotLeft = xMidPoint - 0.5*distanceBtweenX
            yBotLeft = yMidPoint - 0.5*distanceBtweenY

            xTopLeft = xMidPoint - 0.5*distanceBtweenX
            yTopLeft = yMidPoint + 0.5*distanceBtweenY

            a = Grid(xMidPoint,yMidPoint,xTopRight,yTopRight)
            b = Grid(xMidPoint,yBotRight,xBotRight,yMidPoint)
            c = Grid(xBotLeft,yBotLeft,xMidPoint,yMidPoint)
            d = Grid(xTopLeft,yMidPoint,xMidPoint,yTopLeft)

            workingGridList.append(a)
            workingGridList.append(b)
            workingGridList.append(c)
            workingGridList.append(d)

            workingGridList = workingGridList[1:]

        elif workingGridList[0].maxNode(pointList) == 'TurnDown':
            finalGridList.append(workingGridList[0])
            workingGridList = workingGridList[1:]
    return finalGridList





