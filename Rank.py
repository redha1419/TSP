from Point import *
import math
def rank(points):
    points = rankNearby(points)
    points = rankDistance(points)

    for point in points:
        rank = (point.getNearby()/point.getDistance())
        point.setRank(rank)

    return points

def rankNearby(points):
    for i in range(len(points)):
        #temporary for testing
        #points[i].setRadius(15);

        x1 = points[i].getPosition()[0]
        y1 = points[i].getPosition()[1]

        nearby = 0

        for j in range(len(points)):
            if j != i:
                x2 = points[j].getPosition()[0]
                y2 = points[j].getPosition()[1]
                #checking if point is in between x axis
                comparison1 = x2 <= (x1 + points[i].getRadius()) and x2 >= x1
                comparison2 = x2 >= (x1 - points[i].getRadius()) and x2 <= x1
                #checking if point is in between y axis.
                comparison3 = y2 <= (y1 + points[i].getRadius()) and y2 >= y1
                comparison4 = y2 >= (y1 - points[i].getRadius()) and y2 <= y1

                if ((comparison1 or comparison2) and (comparison3 or comparison4)):
                    nearby = nearby + 1
                    points[i].setNearby(nearby)
    return points

def rankDistance(points):
    reference = points[0]
    x1 = reference.getPosition()[0]
    y1 = reference.getPosition()[1]
    points[0].setDistance(-1) #the line that made me go insane

    for i in range(1,len(points)):
        x2 = points[i].getPosition()[0]
        y2 = points[i].getPosition()[1]
        distance = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
        points[i].setDistance(distance)

    return points
