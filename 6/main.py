from numpy import prod
test_races = {7: 9, 15: 40, 30: 200}
races = {54: 239, 70: 1142, 82: 1295, 75:1253}
races_test_part2 = {71530: 940200}
races_part2 = {54708275: 239114212951253}

all_races_beating_races = []
for time, distance in races_part2.items():
    print(time, distance)
    beating_races = []
    for i in range(time):
        time_held_button = i # Speed
        time_left = time - i
        distance_covered = time_held_button*time_left
        if distance_covered > distance:
            beating_races.append(time_held_button)
    all_races_beating_races.append(len(beating_races))

print(prod(all_races_beating_races))
