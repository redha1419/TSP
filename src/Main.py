from Point import *
from Rank import *
from Grid import *
from GridRefine import *
from shapely.geometry import LineString
import random
import math
import sys

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    #generates and creates a point list with IDs and coordinates
    #randomPoints("pointsNew.txt", 40)

    pointsFixed = pointsReader("DjiboutiPoints.txt")
    toDisplay = pointsFixed

    #grids a cartesian "map"
    finalGridList = Refine(Grid(11000,42100,12700,43800.0),pointsFixed)
    lengthFixed = len(pointsFixed)
    minDistance = sys.maxint
    iteration = 0
    for i in range( lengthFixed ):
        points = pointsFixed #does this work lmao?, like dont want to mess with pointsFixed

        #swap iteration
        points[0], points[i] = points[i], points[0]

        #finds how far each point is from starting point
        points =  rankToFirst(pointsFixed)

        #goes thorugh and sorts the list using the "algorithm"
        final = []
        length = len(points)
        while len(final) != length:
            points = rank(points)
            points = logic(points)
            final.append(points[0])
            points = points[1:]

        #set the ending point a.k.a the first point in the list
        fx,fy = final[0].getPosition()

        #connects last node  (fx,fy)
        finalPoint = Point()
        finalPoint.setPosition([fx,fy])
        finalPoint.setId(length+1)
        final.append(finalPoint)

        print str(i) + " -  "+ str(distanceCalc(final))
        if (minDistance > distanceCalc(final) ):
            minDistance = distanceCalc(final)
            toDisplay = final
            iteration = i

    #toDislpay = crissCross(toDisplay)
    #displays results using matplotlib
    displayResults(toDisplay, finalGridList, iteration, minDistance)

def pointsReader(fileName):
    pointsFile = open(fileName,"r")

    points = []
    i = 1
    for line in pointsFile:
        p = Point()
        coords = line.split(",")
        coords[0] = float(coords[0])
        coords[1] = float(coords[1])
        p.setPosition(coords)
        p.setId(i)
        points.append(p)
        i = i+1

    pointsFile.close()
    return points

def logic(points):
    #points.sort(key=lambda x: x.distance, reverse=False)
    return sorted(points, key=lambda x: x.rank, reverse=False)

def randomPoints(fileName, num):
    f = open(fileName, 'w')
    for i in range(num):
        f.write(str(random.randint(0,100)))
        f.write(",")
        f.write(str(random.randint(0,100)))
        f.write("\n")
    f.close()

def rankToFirst(points1):
    points = points1
    x1 = points[0].getPosition()[0]
    y1 = points[0].getPosition()[1]

    for point in points:
        x2 = point.getPosition()[0]
        y2 = point.getPosition()[1]
        distance = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
        point.setToReturn(distance)

    return points

def distanceCalc(points):
    distance = 0
    for i in range(len(points) -1):
        x1 = points[i].getPosition()[0]
        y1 = points[i].getPosition()[1]
        x2 = points[i+1].getPosition()[0]
        y2 = points[i+1].getPosition()[1]
        step = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        distance = distance + step
    return distance

def displayResults(final,finalGridList, iteration, minDistance):

    print "iteration: " + str(iteration) + ", " + "the shortest distance found was " + str(minDistance) + " units." 

    x = []
    y = []
    colors = []
    for point in final:
        x.append(point.getPosition()[0])
        y.append(point.getPosition()[1])
        colors.append(point.getColor())
        #print point.getColor()
    
    #plt.figure(1)
    plt.figure(1)
    #ax = fig.add_subplot(111, projection = '3d')

    for i in range(len(x)):
        plt.scatter(x[i], y[i], color=colors[i])
    plt.plot(x, y)
    #plt.show()
    #plt.plot(x,y,colors,'-o')

    plt.figure(2)
    plt.ylim(ymin = 0.0,ymax = 100)
    plt.xlim(xmin = 0.0,xmax = 100)
    for sq in finalGridList:
        xp = sq.x1
        yp = sq.y1
        xdiff = sq.x2 - sq.x1
        ydiff = sq.y2 - sq.y1
        
        currentAxis = plt.gca()
        currentAxis.add_patch(patches.Rectangle((xp, yp), xdiff, ydiff, fill=None, alpha=1))

    plt.show()

def crissCross(points):
    #this is not a good function! it has an n^2...and ifs lol  complexity! ... fml
    for i in range(len(points)-1):
        reference1 = points[i].getPosition()
        reference2 = points[i+1].getPosition()
        line1 = LineString([reference1,reference2])
        #L1 = line(reference1, reference2)
        for j in range(len(points)-1):
            if i != j:     
                next1 = points[j].getPosition()
                next2 = points[j+1].getPosition()
                line2 = LineString([next1, next2])
                #L2 = line(next1, next2)
                #R = intersection(L1, L2)
                P = line1.intersection(line2)
                try:
                    R = []
                    R.append(P.x)
                    R.append(P.y)
                except AttributeError:
                    R = [-1,-1]     
                if (reference1[0] < R[0] < reference2[0] and reference1[1] < R[1] <  reference2[1]) or (next1[0] < R[0] < next2[0] and next1[1] < R[1] <  next2[1]) :
                    print "yo"
                    points[i].setColor('r')
                    points[i+1].setColor('r')
                    points[j].setColor('r')
                    points[j+1].setColor('r')
    #...uhhh fuck
    return points


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return [x,y]
    else:
        return [-1,-1]

main()