import numpy

# Setting up the original 'theta', 'p', and 'b' matrices
t = [[0], [0]]
p = [[1, 0], [0, 1]]
b = [[0], [0]]


# Preform either recursive or forgetting least squares using sherman-morrison formula
def recurse_ls(player_x, player_y, val):
    global b, t

    # Transforming the 'p' array
    x_arr = player_x
    top = numpy.matmul(numpy.matmul(numpy.matmul(p, x_arr), numpy.transpose(x_arr)), p)
    bottom = val + numpy.matmul(numpy.matmul(numpy.transpose(x_arr), p), x_arr)[0]

    # Calculating new values for 'p' array
    for i in range(2):
        for j in range(2):
            top[i][j] = top[i][j] * bottom
            p[i][j] = p[i][j] - top[i][j]
            p[i][j] = p[i][j] / val

    # Calculating new values for 'b' array & combing 'b' and 'p'
    xy = numpy.matmul(player_x, player_y)
    b = [[b[0][0] + xy[0][0]], [b[1][0] + xy[1][0]]]
    t = numpy.matmul(p, b)
    return t
