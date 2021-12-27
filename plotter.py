import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


def write_plots(steals, gifts, values):

    plt.plot(np.linspace(1, len(steals), len(steals)), steals)
    plt.savefig("data/steals.png")
    plt.clf()

    plt.plot(np.linspace(1, len(gifts), len(gifts)), gifts)
    plt.savefig("data/gifts.png")
    plt.clf()

    x, y = [x[0] for x in values], [x[1] for x in values]
    plt.scatter(x, y)
    plt.annotate(
        "r-squared = {:.3f}".format(
            r2_score([x[0] for x in values], [x[1] for x in values])
        ),
        (0, max(y)),
    )
    plt.savefig("data/values.png")
    plt.clf()
