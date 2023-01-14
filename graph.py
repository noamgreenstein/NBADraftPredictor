import matplotlib.pyplot as graph
import draftPredictor
import leastSquares as rls
import playerDatabase as pd

theta = [0, 0]


def get_it_done(players, y, test, test_y, name, pos):
    x_plot = [0 for x in players]
    x_data = [[0, 0] for x in players]

    for p in range(len(players)):
        temp = draftPredictor.get_x_arr(players[p])
        x_plot[p] = temp[1]
        x_data[p] = temp

    graph.scatter(x_plot, y, label="Training Data")

    for l in range(len(players)):
        global theta
        theta = rls.recurse_ls(x_data[l], y, 1)

    rls_x_plot = [0 for i in range(70)]

    for a in range(len(players)):
        rls_x_plot[a] = theta[a][0] + (theta[a][1] * x_plot[a])

    graph.plot(rls_x_plot, y, label="Recursive Least Squares")

    test_x = [draftPredictor.get_x_arr(players[x])[1] for x in test]
    graph.plot(test_x, test_y)

    graph.title(pos + " MSE: " + get_mse(test_x, test_y, theta, test_y.length))
    graph.xlabel("Recursive Least Squares formula y = \t +\tx")
    graph.ylabel(name)
    graph.show()


def get_mse(players, y, thta, length):
    sum = 0
    for i in range(length):
        pred = thta[0] + thta[1] * players[i]
        sum += (y[i] - pred) ** 2
    return sum / length


training_set = pd.training_2007
y_array = [draftPredictor.get_y_arr(player.tenyr_p) for player in training_set]
x_test_data = [
    draftPredictor.Player(1, 14.9, 4.5, 4.7, .477, 1.2, .38, 9364, 1770, 2836, 379, 176, 3, 1),
    draftPredictor.Player(2, 26.2, 12.4, 1.2, .523, 1.27, 1.64, 6420, 2801, 763, 336, 304, 0, 0),
    draftPredictor.Player(1, 20.7, 4.5, 3.3, .442, 1.55, 0.39, 7574, 1706, 1607, 559, 141, 0, 0),
    draftPredictor.Player(1, 8.3, 2.4, 2.5, .464, 1.03, 0.11, 17184, 4953, 6113, 1300, 217, 7, 7),
    draftPredictor.Player(2, 17.5, 10.6, 1.9, .559, 0.69, 1.4, 11632, 7158, 1471, 447, 298, 5, 2),
    draftPredictor.Player(1, 20.9, 3.3, 2.4, .433, 1.3, 0.63, 9394, 1421, 1713, 535, 187, 0, 0),
    draftPredictor.Player(2, 12.1, 4.8, 2.0, .447, 0.60, 1.2, 282, 120, 44, 16, 30, 0, 0),
    draftPredictor.Player(1, 16.9, 2.9, 6.2, .443, 1.4, 0.04, 6980, 1318, 2778, 436, 25, 0, 0),
    draftPredictor.Player(3, 16, 7.1, 1.1, .480, 0.57, 1.9, 11405, 4299, 993, 358, 1070, 1, 0),
    draftPredictor.Player(1, 19.7, 2.9, 4.0, .458, 0.97, 0.1, 4700, 1173, 1555, 352, 71, 0, 0)]
y_test_data = [draftPredictor.get_y_arr(player.tenyr_p) for player in x_test_data]
get_it_done(training_set, y_array, x_test_data, y_test_data, "10 Year Point Totals",
            "All Positions")
