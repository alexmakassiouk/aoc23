from functools import cmp_to_key


with open('7/data.txt') as f:
    lines = f.readlines()


card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
type_order = ["5kind", "4kind", "fullhouse", "3kind", "2pair", "pair", "highcard"]
hands_bets = {}
for line in lines:
    hands_bets[line.split(" ")[0].strip()] = int(line.split(" ")[1].strip())

def camel_card_sort(hand1: str, hand2: str):
    hand_types = {hand1: "highcard", hand2: "highcard"}
    for hand in [hand1, hand2]:
        if len(set(hand)) == 1:
            hand_types[hand] = "5kind"
        elif len(set(hand)) == 2:
            hand_types[hand] = "4kind" if (hand.count(hand[0]) == 4 or hand.count(hand[1]) == 4) else "fullhouse"
        elif len(set(hand)) == 3:
            hand_types[hand] = "3kind" if (hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3) else "2pair"
        elif len(set(hand)) == 4:
            hand_types[hand] = "pair"
    if hand_types[hand1] != hand_types[hand2]:
        return type_order.index(hand_types[hand1]) - type_order.index(hand_types[hand2])
    else:
        first_card = card_order.index(hand1[0]) - card_order.index(hand2[0])
        if first_card != 0:
            return first_card
        else:
            second_card = card_order.index(hand1[1]) - card_order.index(hand2[1])
            if second_card != 0:
                return second_card
            else:
                third_card = card_order.index(hand1[2]) - card_order.index(hand2[2])
                if third_card != 0:
                    return third_card
                else:
                    fourth_card = card_order.index(hand1[3]) - card_order.index(hand2[3])
                    if fourth_card != 0:
                        return fourth_card
                    else:
                        fifth_card = card_order.index(hand1[4]) - card_order.index(hand2[4])
                        return fifth_card
hands = list(hands_bets.keys())

cmp = cmp_to_key(camel_card_sort)
rankings = {}
hands.sort(key=cmp, reverse=True)
for hand in hands:
    rankings[hand] = hands.index(hand)+1

result = 0
for hand, rank in rankings.items():
    result+= rank*hands_bets[hand]
print(rankings)
print(hands)
print(result)