class Player:

    def __init__(self, player_name, player_points):
        self.player_name = player_name
        self.player_points = player_points

    def points_count(self):
        self.player_points += 15


player_1 = Player('Maks', 0)
player_2 = Player('Oleg', 0)

print(f'{player_1.player_name} : {player_1.player_points}\n'
      f'{player_2.player_name} : {player_2.player_points}')


def count():
    command = int(input())
    while player_1.player_points or player_2.player_points == 45:
        if command == '1':
            player_1.player_points += 15
        if command == '2':
            player_2.player_points += 15
        print(f'{player_1.player_name} : {player_1.player_points}\n'
              f'{player_2.player_name} : {player_2.player_points}')


count()

