# Problem 4.4. Compute the area of an arbitrary triangle

#The following part can be used to insert our own vertices and compute the area.
#Terminal: for example: python triangle_area.py 0 23 9 6 3 7
#It is not handled for Value, Index or other errors though.
# import sys
# x1 = float(sys.argv[1])
# y1 = float(sys.argv[2])
# x2 = float(sys.argv[3])
# y2 = float(sys.argv[4])
# x3 = float(sys.argv[5])
# y3 = float(sys.argv[6])
#
# v1 = []
# v1.append(x1)
# v1.append(y1)
#
# v2 = []
# v2.append(x2)
# v2.append(y2)
#
# v3 = []
# v3.append(x3)
# v3.append(y3)
#
# vertices = []
# vertices.append(v1)
# vertices.append(v2)
# vertices.append(v3)

def triangle_area(vertices):
    """
    Function that returns the area of a triangle
    whose vertices are specified by the argument vertices,
    which is a nested list of the vertex coordinates
    """
    A = 1/2*abs(vertices[1][0]*vertices[2][1] - vertices[2][1]*vertices[1][1] - vertices[0][0]*vertices[2][1] + vertices[2][0]*vertices[0][1] + vertices[0][0]*vertices[1][1] - vertices[1][0]*vertices[0][1])
    return A

# result= triangle_area(vertices)
# print(result)

def test_triangle_area():
    """
    Verify the area of a triangle with vertices (0,0), (1,0), and (0,2).
    """
    v1 = [0,0]; v2 = [1,0]; v3 = [0,2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg

if __name__ == "__main__":
    test_triangle_area()


"""pytest in the terminal:
collected 1 item

triangle_area.py .                                                       [100%]

============================== 1 passed in 0.01s ===============================
"""
