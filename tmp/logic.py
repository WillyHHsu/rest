import random

def shuffle(*players):
    players=[x for x in players]
    
    number_players = len(players)
    random.shuffle(players)
    if number_players%2==0:
        players
    else:
        players.append(players[-1])

    number_games = [x for x in range(1,number_players)]
    pairs_list=[(players [i],players [i+1]) for i in range(0, len(players)-1, 2)]
    games= [(a,b) for a,b in zip(pairs_list,reversed(number_games))]
    return games