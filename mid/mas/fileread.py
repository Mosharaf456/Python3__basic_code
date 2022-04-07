import os
import linecache
from tkinter.constants import X




class Layout:
    """
    A Layout manages the static information about the game board.
    """

    def __init__(self, layoutText):
        self.width = len(layoutText[0])
        self.height = len(layoutText)
        self.walls = Grid(self.width, self.height, False)
        self.food = Grid(self.width, self.height, False)
        self.capsules = []
        self.agentPositions = []
        self.numGhosts = 0
        self.processLayoutText(layoutText)
        self.layoutText = layoutText
        self.totalFood = len(self.food.asList())

    def __str__(self):
        return "\n".join(self.layoutText)


    def processLayoutText(self, layoutText):
        """
        Coordinates are flipped from the input format to the (x,y) convention here

        The shape of the maze.  Each character
        represents a different type of object.
         % - Wall
         . - Food
         o - Capsule
         G - Ghost
         P - Pacman
        Other characters are ignored.
        """
        maxY = self.height - 1
        for y in range(self.height):
            for x in range(self.width):
                layoutChar = layoutText[maxY - y][x]
                self.processLayoutChar(x, y, layoutChar)
        self.agentPositions.sort()
        self.agentPositions = [(i == 0, pos) for i, pos in self.agentPositions]

    def processLayoutChar(self, x, y, layoutChar):
        if layoutChar == '%':
            self.walls[x][y] = True
        elif layoutChar == '.':
            self.food[x][y] = True
        elif layoutChar == 'o':
            self.capsules.append((x, y))
        elif layoutChar == 'P':
            self.agentPositions.append((0, (x, y)))
        elif layoutChar in ['G']:
            self.agentPositions.append((1, (x, y)))
            self.numGhosts += 1
        elif layoutChar in ['1', '2', '3', '4']:
            self.agentPositions.append((int(layoutChar), (x, y)))
            self.numGhosts += 1


def getLayout(name, back=2):
    if name.endswith('.lay'):
        layout = tryToLoad('layouts/' + name)
        if layout == None:
            layout = tryToLoad(name)
    else:
        layout = tryToLoad('layouts/' + name + '.lay')
        if layout == None:
            layout = tryToLoad(name + '.lay')
    if layout == None and back >= 0:
        curdir = os.path.abspath('.')
        os.chdir('..')
        layout = getLayout(name, back - 1)
        os.chdir(curdir)
    return layout


def tryToLoad(fullname):
    if(not os.path.exists(fullname)):
        return None
    f = open(fullname)
    try:
        return Layout([line.strip() for line in f])
    finally:
        f.close()


class Grid:
    """
    A 2-dimensional array of objects backed by a list of lists.  Data is accessed
    via grid[x][y] where (x,y) are positions on a Pacman map with x horizontal,
    y vertical and the origin (0,0) in the bottom left corner.

    The __str__ method constructs an output that is oriented like a pacman board.
    """

    def __init__(self, width, height, initialValue=False, bitRepresentation=None):
        if initialValue not in [False, True]:
            raise Exception('Grids can only contain booleans')
        self.CELLS_PER_INT = 30

        self.width = width
        self.height = height
        self.data = [[initialValue for y in range(height)] for x in range(width)]
        if bitRepresentation:
            self._unpackBits(bitRepresentation)

    def __getitem__(self, i):
        return self.data[i]


    def asList(self, key=True):
        list = []
        for x in range(self.width):
            for y in range(self.height):
                if self[x][y] == key:
                    list.append((x, y))
        return list





    def _unpackBits(self, bits):
        """
        Fills in data from a bit-level representation
        """
        cell = 0
        for packed in bits:
            for bit in self._unpackInt(packed, self.CELLS_PER_INT):
                if cell == self.width * self.height:
                    break
                x, y = self._cellIndexToPosition(cell)
                self[x][y] = bit
                cell += 1






def createLayout(y):
    x = y
    a=getLayout(x)
    #print(a)
    # print(type(a))

    ## file write
    fileref=open("a.txt",'w')
    x = str (a)
    fileref.write(x)
    fileref.close()

    fileref=open("a.txt",'r')
    contents=fileref.read()


    line_count = 0
    li=[]
    for i in contents.split('\n'):
        li.append(i)
        line_count += 1

    #print (line_count)

    char = 0
    for i in range(1):
        ab = li[i]
        for a in ab:
            char += 1
    
    #print (char)
    
    ab=''
    tutorial=[]
    num=0

    for i in li:
        ab=i
        for a in ab:
            if a=='%':
                 tutorial.append(num)
                 num+=1
            if a=='.':
                 num+=1
            if a==" ":
                 num+=1
            if a=='P':
                 num+=1
            if a=='o':
                 num+=1
            if a=='G':
                num+=1

            
        
    return tutorial
    fileref.close()


def findrc(y):
    a=getLayout(y)
    #print(a)
    # print(type(a))

    ## file write
    fileref=open("b.txt",'w')
    x = str (a)
    fileref.write(x)
    fileref.close()

    
    fileref=open("b.txt",'r')
    contents=fileref.read()


    line_count = 0
    li=[]
    for i in contents.split('\n'):
        li.append(i)
        line_count += 1

    #print (line_count)

    char = 0
    for i in range(1):
        ab = li[i]
        for a in ab:
            char += 1
    
    #print (char)

    row_col = [0,1]
    row_col[0] = line_count
    row_col[1] = char          
        
    return row_col
    fileref.close()

# z = createLayout ('bigSearch')
# p = findrc('bigSearch')

# print (p)
# print (z)



        











