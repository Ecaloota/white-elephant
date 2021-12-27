def logistic_activation(x):
    """
    Logistic activation function over [0,1].
    Returns the probability of an action.
    We treat x as an input between [0, 1].
    """

    # x = 1 or x > 1
    if (1 - x) == 0 or x > 1:
        return 1

    if x == 0 or x < 0:
        return 0

    return 1 / (1 + 1 / (x / (1 - x)) ** 2)
