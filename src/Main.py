from Point import *
from Rank import *
from Grid import *
from GridRefine import *
import random

import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    #randomPoints("points.txt", 20)

    points = pointsReader("points.txt")
    points =  rankToFirst(points)
    finalGridList = Refine(Grid(0.0,0.0,100.0,100.0),points)
    fx,fy = points[0].getPosition()
    final = []
    length = len(points)
    while len(final) != length:
        points = rank(points)
        points = logic(points)
        final.append(points[0])
        points = points[1:]

    for point in final:
        print "( ", point.getPosition()[0], " ", point.getPosition()[1], " ) - ", point.getDistance()

    x = []
    y = []

    for point in final:
        x.append(point.getPosition()[0])
        y.append(point.getPosition()[1])

    x.append(fx)
    y.append(fy)
    
    plt.figure(1)
    plt.plot(x,y,'-o')

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

def pointsReader(fileName):

    pointsFile = open(fileName,"r")

    #num_lines = sum(1 for line in open(fileName)) number of lines in file

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

def rankToFirst(points):
    x1 = points[0].getPosition()[0]
    y1 = points[0].getPosition()[1]

    for point in points:
        x2 = point.getPosition()[0]
        y2 = point.getPosition()[1]
        distance = math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
        point.setToReturn(distance)

    return points

main()
