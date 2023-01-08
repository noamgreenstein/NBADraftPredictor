import matplotlib.pyplot as graph
import draftPredictor
import leastSquares as rls

theta = [0, 0]


def get_it_done(players, y, test):
    x_plot = [0 for x in players]
    x_data = [[0, 0] for x in players]

    for p in players:
        temp = draftPredictor.get_x_arr(players[p])
        x_plot[p] = temp[1]
        x_data[p] = temp

    graph.scatter(x_plot, y, label="Training Data")

    for l in players:
        global theta
        theta = rls.recurse_ls(x_data[l], y)

    rls_x_plot = [0 for i in range(70)]

    for a in players:
        rls_x_plot[a] = theta[a][0] + (theta[a][1] * x_plot[a])

    graph.plot(rls_x_plot, y, label="Recursive Least Squares")

    test_x = [0 for x in players]
