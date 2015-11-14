from datetime import datetime, timedelta
import misc
# id,  player1,  player_1_shots,  player_1_hits,   player2,  player_2_shots,  player_2_hits,  winner,  time,  date
class Score:
    def __init__(self, gameID, player_1, player_1_shots, player_1_hits,
                 player_2, player_2_shots, player_2_shits, winner,
                 time, date):
        self.gameID = gameID

        self.player_1 = player_1
        self.player_1_shots = player_1_shots
        self.player_1_hits = player_1_hits

        self.player_2 = player_2
        self.player_2_shots = player_2_shots
        self.player_2_hits = player_2_shits

        self.winner = winner
        self.time = time
        self.date = date

    def to_dict(self):
        return dict(
            gameID=self.gameID,
            player_1=self.player_1,
            player_2=self.player_2,
            player_1_shots=self.player_1_shots,
            player_2_shots=self.player_2_shots,
            player_1_hits=self.player_1_hits,
            player_2_hits=self.player_2_hits,
            winner=self.winner,
            time=self.time,
            date=self.date
        )
    def __str__(self):
        return "{0:2} {1:10} {2:4} {3:4} {4:10} {5:4} {6:4} {7:2} {8:6} {9}".format(
            self.gameID,
            self.player_1,
            self.player_1_shots,
            self.player_1_hits,
            self.player_2,
            self.player_2_shots,
            self.player_2_hits,
            self.winner,
            self.time,
            self.date
        )

def parse(line):
    d = [x for x in line.split(" ") if x != ""]
    return Score(d[0], d[1], int(d[2]), int(d[3]), d[4], int(d[5]), int(d[6]), int(d[7]), int(d[8]), d[9])


def from_game(game, board1, board2):
    """
    :type game: Game.Game
    :type winner: int
    :type return: Score
    """
    cells1 = reduce(list.__add__, board1)
    cells2 = reduce(list.__add__, board2)
    player_1_shots = len([x for x in cells2 if x%misc.SHOT == 0])
    player_2_shots = len([x for x in cells1 if x%misc.SHOT == 0])
    player_1_hits = len([x for x in cells2 if x%misc.SHOT == 0 and x%misc.SHIP == 0])
    player_2_hits = len([x for x in cells1 if x%misc.SHOT == 0 and x%misc.SHIP == 0])
    delta_time = misc.get_unix_timestamp() - game.started_at
    winner = 1 if player_1_hits > player_2_hits else 2
    return Score(game.gameID,
                 game.player_1, player_1_shots, player_1_hits,
                 game.player_2, player_2_shots, player_2_hits,
                 winner, delta_time, unix_to_timestamp(game.started_at))


def unix_to_timestamp(unixTime):
    UNIX_EPOCH = datetime(year=1970, month=1, day=1)
    actual_time = UNIX_EPOCH + timedelta(seconds=unixTime)
    return actual_time.isoformat()