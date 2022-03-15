# White Elephant Simulator

Feeling the Christmas spirit? This is a numerical simulation of the popular Christmas gift-stealing game White Elephant.

In our version of the game, players bring wrapped gifts and place them in a pile; drawing player order randomly (from a hat), players take turns to either take a wrapped gift from the pile, or steal an unwrapped gift from another player who has previously taken or stolen that gift.

The rules can vary (see [here](https://www.whiteelephantrules.com/)), but currently we only support "three steals and the gift is out-of-play". We place no restrictions on the number of steals per turn.

### Features

* Value-biased: NPC choices (whether to steal or take a gift) can be either random (flip a coin), or probabilistic (depending upon the quality of gifts that have been revealed)

## Installation

```
pip install -r requirements.txt
```

## Usage

Suppose you wanted to run a simulation of 100 games, each with 10 players:

```
python3 main.py --rounds 100 --players 10
```

You could also elect to print key statistics from these games (the average value of gifts obtained by each player; the average number of times each player steals; and, the relationship between gift quality and the number of times that gift is stolen) by invoking the --write and/or --plot flags. See below usage example:

```
> python3 main.py -h

usage: main.py [-h] [-v] [-u] [-r ROUNDS] [-n PLAYERS] [-w WRITE] [-p PLOT]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         make verbose
  -u, --unbiased        whether npc choices are biased by gift values. if False, results are biased
  -r ROUNDS, --rounds ROUNDS, --games ROUNDS
                        the number of games to play
  -n PLAYERS, --players PLAYERS
                        the number of players per game
  -w WRITE, --write WRITE, --output WRITE
                        to write outputs or not
  -p PLOT, --plot PLOT  to write plots or not
``` 