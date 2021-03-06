from Point import *
import math
def rank(points):
    points = rankNearby(points)
    points = rankDistance(points)

    for point in points:
        # The equation below found the fifth best distance for a randomly selected constant set of points
        #rank = (point.getNearby()**(1/2.0))*(point.getDistance())**2 - point.getToReturn()

        # The equation below found the fourth shortest distance so far
        #rank = math.sqrt(math.log(point.getNearby() + 1))*(point.getDistance())**2 - point.getToReturn()

        # This equation tied for the fourth shortest distance so far
        #rank = math.sqrt(math.log(point.getNearby() + 1))*(point.getDistance())**2 - point.getToReturn()**(1/2.0)

        # This one found the third best so far
        #rank = math.exp(math.log(point.getNearby() + 1))*(point.getDistance())**(2) - point.getToReturn()**(1/2.0)

        # This found the second shortest distance for this set so far
        #rank = math.exp(math.log(point.getNearby() + 1))*(point.getDistance()**3) - point.getToReturn()**(1/2.0)

        # This one found the shortest distance so far
        #rank = math.exp(math.log(point.getNearby() + 1))*(point.getDistance()**5) - point.getToReturn()**(1/2.0)


        rank = math.exp(math.log(point.getNearby() + 1))*(point.getDistance()**5) - point.getToReturn()**(1/2.0)
        point.setRank(rank)

    return points

def rankNearby(points):
    for i in range(len(points)):
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

