with open('4/data.txt') as f:
    lines = f.readlines()

total_points = 0
for line in lines:
    card_points = 0
    winning_numbers = line.split(":")[1].split("|")[0].strip().split(" ")
    winning_numbers = [winning_number for winning_number in winning_numbers if winning_number != ""]
    my_numbers = line.split(":")[1].split("|")[1].strip().split(" ")
    my_numbers = [my_number for my_number in my_numbers if my_number != ""]
    for number in my_numbers:
        if number in winning_numbers:
            card_points+= 1
    if card_points > 0:
        total_points += 2**(card_points-1)
print(total_points)

# Part 2

def get_card_points(card_line):
    card_points = 0
    winning_numbers = card_line.split(":")[1].split("|")[0].strip().split(" ")
    winning_numbers = [winning_number for winning_number in winning_numbers if winning_number != ""]
    my_numbers = card_line.split(":")[1].split("|")[1].strip().split(" ")
    my_numbers = [my_number for my_number in my_numbers if my_number != ""]
    for number in my_numbers:
        if number in winning_numbers:
            card_points+= 1
    return card_points

card_copies = {}
for card_index, original_card in enumerate(lines):
    card_number = card_index+1
    card_points = get_card_points(original_card)

    for i in range(card_number+1, card_number+card_points+1):
        card_copies[i] = card_copies.get(i, 0) + 1
    for i in range(card_copies.get(card_number, 0)):
        copy_card_points = get_card_points(original_card)
        for j in range(card_number+1, card_number+card_points+1):
            card_copies[j] = card_copies.get(j, 0) + 1
    card_copies[card_number] = card_copies.get(card_number, 0) + 1
# for key, value in card_copies.items():
#     card_copies[key]+=1
# Don't forget the original cards
print(card_copies)
sum_cards = 0
for value in card_copies.values():
    sum_cards += value
print(sum_cards)