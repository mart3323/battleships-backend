from obsoleteClasses import Game

TILE = Game.TILE
game = Game.open_game(2)
Game.save_game(game)
