with open('2/data.txt') as f:
    lines = f.readlines()

illegal_game_ids = []

for line in lines:
    game_sets = line.split(":")[1].split(';')
    for game_set in game_sets:
        combinations = game_set.split(',')
        for combination in combinations:
            number, color = combination.strip().split(' ')
            if "red" in color and int(number) >12:
                illegal_game_ids.append(int(line.split(":")[0].split(" ")[1]))
                break
            elif "green" in color and int(number) > 13:
                illegal_game_ids.append(int(line.split(":")[0].split(" ")[1]))
                break
            elif "blue" in color and int(number) > 14:
                illegal_game_ids.append(int(line.split(":")[0].split(" ")[1]))
                break

all_game_ids = sum([i for i in range(1, 101)])
print(all_game_ids)
sum_illegal_game_ids = sum(set(illegal_game_ids))
print(all_game_ids-sum_illegal_game_ids)

# part 2
game_powers = []
for game in lines:
    minimum_amount_of_colors = []
    colors = ["blue", "green", "red"]
    for color in colors:
        amounts_with_noise = game.split(" " + color)
        amounts = [amounts_with_noise[i].split(" ")[-1] for i in range(0, len(amounts_with_noise))]
        try:
            amounts.remove("\n")
        except ValueError:
            pass
        minimum_amount_of_colors.append(max([int(amount) for amount in amounts if amount.isdigit()]))
    game_powers.append(minimum_amount_of_colors[0]*minimum_amount_of_colors[1]*minimum_amount_of_colors[2])
print(sum(game_powers))