import matplotlib.pyplot as graph
import numpy


# Setting up the 'X' matrix
def setupx(xdata, num):
    x = [[0, 0] for k in range(num)]
    for i in range(num):
        for j in range(2):
            if (j == 0):
                x[i][j] = xdata[i] ** 3
            else:
                x[i][j] = xdata[i] ** 6
    return x


# Setting up the 'Y' matrix
def setupy(ydata, num):
    y = [[ydata[n]] for n in range(num)]
    return y


# Calculating the missing values
def calcTheta(x, y):
    xt = numpy.transpose(x)
    xtx = numpy.matmul(xt, x)
    inverse = numpy.linalg.inv(xtx)
    xty = numpy.matmul(xt, y)
    return numpy.matmul(inverse, xty)

# Preform either recursive or forgetting least squares
def recurse_ls(idx, val):
    global b, t

    # Transforming the 'p' array
    x_arr = [[xTraining[idx] ** 3], [xTraining[idx] ** 6]]
    top = numpy.matmul(numpy.matmul(numpy.matmul(p, x_arr), numpy.transpose(x_arr)), p)
    bottom = val + numpy.matmul(numpy.matmul(numpy.transpose(x_arr), p), x_arr)[0]

    # Calculating new values for 'p' array
    for i in range(2):
        for j in range(2):
            top[i][j] = top[i][j] * bottom
            p[i][j] = p[i][j] - top[i][j]
            p[i][j] = p[i][j] / val

    # Calculating new values for 'b' array & combing 'b' and 'p'
    xy = [[(xTraining[idx] ** 3) * yTraining[idx]], [(xTraining[idx] ** 6) * yTraining[idx]]]
    b = [[b[0][0] + xy[0][0]], [b[1][0] + xy[1][0]]]
    t = numpy.matmul(p, b)
    return t