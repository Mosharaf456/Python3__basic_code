from fileread import findrc

global x
x = 'mediumSafeSearch'   ########## Layout Selection 
global row
global col
list1 = [0,1]
list1 = findrc(x)
row = list1[0]
col = list1[1]

def relation(i, j):

    if row>col:
        vertical = row
        vertical_rem = row-1
    if col>row:
        vertical = col
        vertical_rem = col-1
    if row == col:
        vertical = row
        vertical_rem = row-1

    if i == j:                                                          # check whether the vertices are same
        return 0
    if i % vertical != 0 and i % vertical != vertical_rem:              # check not first or last column
        if i+1 == j or i-1 == j or i+vertical == j or i-vertical == j:
            return 1

        else:
            return 0
    elif i % vertical == 0:                                             # if first column
        if i+1 == j or i+vertical == j or i-vertical == j:
            return 1

        else:
            return 0
    elif i % vertical == vertical_rem:                                  # if last column
        if i-1 == j or i+vertical == j or i-vertical == j:
            return 1

        else:
            return 0


r = row
c = col
size = r*c
adjacencey_mat = [[0 for i in range(size)] for j in range(size)]

for i in range(0, size):
    for j in range(0, size):
        result = relation(i, j)
        adjacencey_mat[i][j] = result


def return_matrix():
    return adjacencey_mat, size

