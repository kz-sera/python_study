
import random as rand
#所持金

#キーボード入力の受付

#トランプカード(A~K)のリスト

#トランプカードをランダムで選出するランダム変数

#プレイヤーの手を格納する空のリスト

money = 3000
print('所持金', money)

# bit = int(input('掛け金を入力してください'))
# print('掛け金', bit)

trump_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

trump_rand =rand.randint(0, len(trump_card)-1)

player_hand = []


rand1 = rand.randint(0, len(trump_card)-1)
rand2 = rand.randint(0, len(trump_card)-1)

trump_1 = trump_card[rand1]
trump_2 = trump_card[rand2]

player_hand.append(trump_1)
player_hand.append(trump_2)
print(player_hand)

point_1 = 0
point_eleven = 0
for card in player_hand:
    if card == 'A':
        point_1 += 1
        point_eleven += 11
    elif card == 'J':
        point_1 += 10
        point_eleven += 10
    elif card == 'Q':
        point_1 += 10
        point_eleven += 10
    elif card == 'K':
        point_1 += 10
        point_eleven += 10
    else:
        point_1 += int(card)
        point_eleven += int(card)
print(point_1)
print(point_eleven)

if point_eleven == 21:
    print('ブラック・ジャックだ!!')