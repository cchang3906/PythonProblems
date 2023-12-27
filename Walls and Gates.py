# --A function that solves the problem that takes an array as input and returns the desired
#   output array
# --A main function that runs that function on both the example inputs AND another sample 
#   input you write yourself
# --The main function should print the inputs and outputs for each example.
INF = 2147483647
rooms = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
output = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
m = len(rooms)
n = len(rooms[0])

def dist(rooms):
    for i in range(len(rooms)):
        for j in range(len(rooms[i])):
            if rooms[i][j]==-1:
                output[i][j]=-1
            probe(rooms, i, j)
            print(output[2][0], output[1][0], output[3][2], output[3][3])


def probe(rooms, i, j):
    if i>=0 and i<m and j>=0 or j<n:
        if rooms[i][j]==0:
            if j-1>=0 and rooms[i][j-1]==INF:
                output[i][j-1]=output[i][j]+1
            if i-1>=0 and rooms[i-1][j]==INF:
                output[i-1][j]=output[i][j]+1
            if j+1<n and rooms[i][j+1]==INF:
                output[i][j+1]=output[i][j]+1
            if i+1<m and rooms[i+1][j]==INF:
                output[i+1][j]=output[i][j]+1
        elif output[i][j]==1:
            if j-1>=0 and rooms[i][j-1]==INF:
                output[i][j-1]= output[i][j]+1
            if rooms[i-1][j]==INF:
                output[i-1][j]= output[i][j]+1
            if j+1<n and rooms[i][j+1]==INF:
                output[i][j+1]= output[i][j]+1
            if i+1<m and rooms[i+1][j]==INF:
                output[i+1][j]= output[i][j]+1
        elif output[i][j]>1 and output[i][j]<INF:
            if j-1>=0 and output[i][j-1]==0:
                output[i][j-1]= output[i][j]+1
            if i-1>=0 and output[i-1][j]==0:
                output[i-1][j]= output[i][j]+1
            if j+1<n and output[i][j+1]==0:
                output[i][j+1]= output[i][j]+1
            if i+1<m and output[i+1][j]==0:
                output[i+1][j]= output[i][j]+1
    else:
        return

dist(rooms)
#print("Input: rooms = [[INF, -1, 0, INF], [-1, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]")
for i in range(len(output)):
    for j in range(len(output[i])):
        print(output[i][j], end=' ')
    print("\n")