# Problem 6.14. Plotting graphs

import matplotlib.pyplot as plt
from math import sqrt

#a)
def plot_line(p1,p2):

    plt.plot([p1[0], p2[0]],  [p1[1], p2[1]])
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Line between two points")
    return plt.show()

h1 = [-4,6] ; h2 = [1,1]   # random coordinates for horizontal line
v1 = [1,1]  ; v2 = [5,-2]  # random coordinates for vertical line

horizontal = plot_line(h1,h2)
vertical = plot_line(v1,v2)

#b)
#modified plot from a)
def plot_line(p1,p2):
    plt.plot(p1, p2, 'b-o', markerfacecolor = 'red',markeredgecolor = 'red',markersize=6)

def complete_graph(points):
    index = len(points)

    #looping over all point combinations
    for i in range(0, index):
        for j in range(0, index):
            if (j!=i):
                plot_line((points[i][0],points[j][0]), (points[i][1],points[j][1]))

    plt.xlabel("x")
    plt.ylabel("y")

    #do not show ticks on y axis
    ax = plt.gca()
    ax.axes.yaxis.set_ticks([])
    return plt.show()

square = [(0, 0), (1, 0), (0, 1), (1, 1)]
p1= complete_graph(square)

α = sqrt(2)/2
circle = [(1,0),(α,α),(0,1),(-α,α),(-1,0),(-α,-α),(0,-1),(α,-α)]
p2= complete_graph(circle)
