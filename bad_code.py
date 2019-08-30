
player_data = [ 
    ( 1000, 1.5 ),
    ( 1200, 0.5 ),
    ( 1800, 1.1 ),
    ( 700, 2.0 ),
]

print("Initial data = " + str(player_data))

for i in range(0, len(player_data)):
    score, bonus = player_data[0]
    score = score + score ** bonus
    bonus = bonus / 2
    player_data[i] = ( score, bonus)

print("Updated data = " + str(player_data))
