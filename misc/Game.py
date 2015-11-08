def parse(line):
    vals = filter(lambda x: x != "", line.replace("\n", "").split(" "))
    gameID, player_1, player_1_hash, player_2, player_2_hash, \
    game_state, waiting_for, num_ships, board_size, started_at = vals
    gameID = int(gameID)
    waiting_for = int(waiting_for)
    num_ships = int(num_ships)
    board_size = int(board_size)

    return dict(gameID=gameID,
                player_1=player_1,
                player_1_hash=player_1_hash,
                player_2=player_2,
                player_2_hash=player_2_hash,
                game_state=game_state,
                waiting_for=waiting_for,
                num_ships=num_ships,
                board_size=board_size,
                started_at=0)


def stringify(gameID, player_1, player_1_hash, player_2, player_2_hash, game_state, waiting_for, num_ships, board_size, started_at):
    return "{:8} {:16} {:8} {:16} {:8} {:8} {:8} {:8} {:8} {:8}".format(
        gameID,
        player_1,
        player_1_hash,
        player_2,
        player_2_hash,
        game_state,
        waiting_for,
        num_ships,
        board_size,
        started_at
    )


class Game:
    def __init__(self, data):
        self.gameID = data["gameID"]
        self.player_1 = data["player_1"]
        self.player_2 = data["player_2"]
        self.player_1_hash = data["player_1_hash"]
        self.player_2_hash = data["player_2_hash"]
        self.game_state = data["game_state"]
        self.waiting_for = data["waiting_for"]
        self.num_ships = data["num_ships"]
        self.board_size = data["board_size"]
        self.started_at = data["started_at"]

    def to_personalized_dict(self, player_id):
        return dict(gameID=self.gameID,
                    your_name=self.player_1 if player_id == 1 else self.player_2,
                    opponent_name=self.player_2 if player_id == 1 else self.player_1,
                    your_hash=self.player_1_hash if player_id == 1 else self.player_2_hash,
                    game_state=self.game_state,
                    waiting_for=self.waiting_for,
                    num_ships=self.num_ships,
                    board_size=self.board_size,
                    started_at=self.started_at
                    )

    def to_dict(self):
        return dict(gameID=self.gameID,
                    player_1=self.player_1,
                    player_2=self.player_2,
                    player_1_hash=self.player_1_hash,
                    player_2_hash=self.player_2_hash,
                    game_state=self.game_state,
                    waiting_for=self.waiting_for,
                    num_ships=self.num_ships,
                    board_size=self.board_size,
                    started_at=self.started_at
                    )
