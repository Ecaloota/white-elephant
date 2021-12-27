from __future__ import annotations
import numpy as np
from collections import Counter

from gift import Gift
from player import Player


def game_loop(num_players: int, verbose: bool = False, value_biased: bool = False):

    PlayerPool = [Player(i) for i in range(num_players)]
    GiftPool = [Gift(i) for i in range(num_players)]

    ## find which gifts are available in the pool
    available_gifts = [i for i in GiftPool]

    for player in PlayerPool:

        if verbose:
            print("#" * 20)
            print("TURN ", player.position + 1)
            print("#" * 20)

        # the first action will always be for the first player to take from the pool
        if player.position == 0:
            available_gifts = player.take_gift_from_pool(GiftPool, verbose=verbose)
            continue

        ## find which other players have gifts that can be stolen
        lootable_players = [
            x
            for x in PlayerPool
            if x.gift is not None
            and x.position != player.position
            and x.gift.times_stolen < 3
        ]

        available_gifts, lootable_players = player.take_or_steal(
            available_gifts, lootable_players, verbose, value_biased
        )

    if verbose:
        print("#" * 20)
        print("GAME OVER!")
        print("#" * 20)

    return PlayerPool, GiftPool


def generate_statistics(n_players, n_rounds, verbose, value_biased):

    players_array = np.empty([n_rounds, n_players], dtype=object)
    for i in range(n_rounds):
        Players, Gifts = game_loop(n_players, verbose, value_biased)
        players_array[i] = Players

    ## the number of steals in each round
    number_steals_array = np.array(
        [player.number_of_steals for row in players_array for player in row]
    ).reshape([n_rounds, n_players])

    ## This is the value of each gift in each round
    player_gifts_array = np.array(
        [int(player.gift.value * 1000 / 10) for row in players_array for player in row]
    ).reshape([n_rounds, n_players])

    ## This is how many times each gift in each round was stolen
    number_times_stolen_array = np.array(
        [player.gift.times_stolen for row in players_array for player in row]
    ).reshape([n_rounds, n_players])

    flat_gifts = np.ravel(player_gifts_array).tolist()
    flat_stolen = np.ravel(number_times_stolen_array).tolist()
    flat_value_by_stolen = list(zip(flat_gifts, flat_stolen))

    count = Counter(flat_gifts)
    # print(count)
    # print("count: ", count[1])
    gift_value_by_stolen_sum = []
    for i in range(1, 101):
        sum = 0
        for k, v in flat_value_by_stolen:
            if k == i:
                sum += v
        gift_value_by_stolen_sum.append((i, sum))

    av_number_steals_per_round = np.average(number_steals_array, axis=1)
    av_number_steals_per_player = np.average(number_steals_array, axis=0)
    av_final_gift_value_per_player = np.average(player_gifts_array, axis=0)
    av_times_stolen_per_gift = np.average(number_times_stolen_array, axis=0)

    normalised_gift_value_by_stolen = [
        (x[0], (x[1] / count[x[0]]) * 100) for x in gift_value_by_stolen_sum
    ]

    return (
        av_number_steals_per_player,  ## Who steals most?
        av_final_gift_value_per_player,  ## Who gets the best gift?
        gift_value_by_stolen_sum,  ## Do better gifts get stolen more?
        normalised_gift_value_by_stolen,
    )
