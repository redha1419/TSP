class Point:

    def __init__(self):
        self.id = 0
        self.radius = 0
        self.nearby = 0
        self.distance = -1
        self.position = [-1,-1]
        self.rank = 0

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def getRank(self):
        return self.rank

    def setRank(self, rank):
        self.rank = rank

    def getNearby(self):
        return self.nearby

    def setNearby(self,nearby):
        self.nearby = nearby

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def setDistance(self, distance):
        self.distance = distance

    def getDistance(self):
        return self.distance