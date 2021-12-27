from __future__ import annotations
from random import choice
import numpy as np

from logistic import logistic_activation


class Player:
    def __init__(self, position: str) -> None:

        self.position = position
        self.gift = None
        self.number_of_steals = 0

    def steal_gift_from_player(
        self,
        player: Player,
        lootable_players: list,
        available_gifts: list,
        verbose: bool = False,
        value_biased: bool = True,
    ):

        ## Steal the gift from the other player
        self.gift = player.gift
        self.number_of_steals += 1
        self.gift.times_stolen += 1

        if verbose:
            print(
                f"Gift {player.gift.index} stolen from {player.gift.current_owner} by {self}!"
            )

        player.gift.current_owner = self
        player.gift = None

        available_gifts, lootable_players = player.take_or_steal(
            available_gifts, lootable_players, verbose, value_biased
        )

        return lootable_players, available_gifts

    def take_gift_from_pool(self, pool: list, verbose: bool = False) -> list:
        """
        Take a Gift from the pool.
        """

        gift = choice(pool)
        pool.remove(gift)
        self.gift = gift
        gift.current_owner = self

        if verbose:
            print(f"Gift {gift.index} taken from GiftPool by Player {self.position}!")

        return pool

    def consider_steal(self, lootable_players, value_biased=True):
        """
        Decide whether to steal on the basis of current game state.
        """

        ## If there is no-one to steal from
        if len(lootable_players) == 0:
            return False

        ## If value-biased, the choice to steal is based on a logistic function that
        ## considers the average quality or maximum quality of the lootable gifts.
        if value_biased and len(lootable_players) != 0:
            values = [x.gift.value for x in lootable_players]
            norm_values = [float(i) / sum(values) for i in values]
            p_steal = float(logistic_activation(np.mean(norm_values)))
            will_steal = np.random.choice([True, False], p=[p_steal, (1 - p_steal)])

        ## Otherwise flip a coin.
        else:
            will_steal = choice([True, False])

        return will_steal

    def take_or_steal(
        self, available_gifts, lootable_players, verbose=False, value_biased=True
    ):
        """
        Given the choice, decide whether to steal from another player or take from the pool.
        """

        will_steal = self.consider_steal(lootable_players, value_biased)

        if will_steal and len(lootable_players) != 0:
            if value_biased:
                values = [x.gift.value for x in lootable_players]
                norm_values = [float(i) / sum(values) for i in values]
                player_to_steal_from = np.random.choice(lootable_players, p=norm_values)

            else:
                player_to_steal_from = choice(lootable_players)

            lootable_players.remove(player_to_steal_from)
            lootable_players, available_gifts = self.steal_gift_from_player(
                player_to_steal_from, lootable_players, available_gifts, verbose=verbose
            )
        else:
            available_gifts = self.take_gift_from_pool(available_gifts, verbose=verbose)

        return available_gifts, lootable_players

    def __repr__(self) -> str:
        return f"Player {self.position}"
