#if公文の練習
# num = 1

# if 1 <= num < 10:
#     print('バナナ')

# print('####################')

# #  keyboard = int(input('あなたの年齢を入力して候'))
# keyboard = 20
# if 20 <= keyboard:
#      print('お酒飲めます')
# else: 
#     print('お酒は飲めません')

# print('####################')

# if 'A' == 'a':
#     print(True)
# else:
#     print(False)

# age = int(input('あなたの年齢を入力して候'))
# if 13 <= age <= 19:
#     print('あなたはティーンエイジャーで候')
# elif age == 20:
#     print('あなたは成人です')
# else:
#     print('あなたはティーンエイジャーではない')

# name = 'sera kazui'
# if False:
#     print('aは含まれます')
# elif 'o' not in name:
#     print('oは含まれません')

import random as rand
money = 3000
print('所持金', money)

bit = int(input('掛け金を入力してください'))
print('掛け金', bit)

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


    