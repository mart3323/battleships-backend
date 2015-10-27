

class Score:
    def __init__(self, board_size, number_of_ships, winner, player_1_shots, player_2_shots, time):
        self.winner = winner
        self.player_1_shots = player_1_shots
        self.player_2_shots = player_2_shots
        self.time = time
        self.number_of_ships = number_of_ships
        self.board_size = board_size

    def __str__(self):
        return "{0:8}|{1:8}|{2:8}|{3:8}|{4:8}|{5:8}".format(
                                                self.board_size,
                                                self.number_of_ships,
                                                self.winner,
                                                self.player_1_shots,
                                                self.player_2_shots,
                                                self.time,
        )

    @classmethod
    def from_string(cls, string):
        string = string.replace(" ", "")
        bs, ns, w, p1s, p2s, t = string.split("|")
        bs, ns, w, p1s, p2s, t = int(bs), int(ns), int(w), int(p1s), int(p2s), float(t)
        return cls(bs, ns, w, p1s, p2s, t)


class RecentScores:
    def __init__(self, scores):
        self.scores = scores

    @classmethod
    def load(self, lines):
        return RecentScores([Score.from_string(x) for x in lines][0:10])

    def write_to(self, file):
        for score in self.scores:
            file.write(str(score)+"\n")

    def add(self, score):
        self.scores.append(score)
        self.scores = self.scores[-10:12]
