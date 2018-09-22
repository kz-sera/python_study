
import random as rand

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(num_list)

# print(num_list[8])
# print(num_list[4])

rand_int = rand.randint(0, 8)
# print('rand_int:', rand_int)
# print(num_list[rand_int])


trump_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
trump_rand =rand.randint(0, len(trump_card)-1)
print(trump_card[trump_rand])

print('####################')

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(num_list)

# print('####################')

# mika_list = ['こ', 'み', 'や', 'ま', 'み', 'か']
# print(mika_list)

# print('####################')

# print(mika_list[3])

# print('####################')

# rand_int = rand.randint(0, 5)
# print(mika_list[rand_int])

player_hand = []
print(player_hand)

one_card = trump_card[trump_rand]

player_hand.append(one_card)
print(player_hand)

player_hand += 'joker'
player_hand += '4', '2'
print(player_hand)

mika_name = []
mika_name += 'こみやまみか'
print(mika_name)

player_hand.extend(mika_name)
print(player_hand)

len_list = len(player_hand)
print(len_list)

fruits_list = ['りんご', 'レモン', 'ぶどう', 'メロン', 'いちご', 'バナナ', 'バナナ', 'バナナ', 'みかん', 'キウイ', 'りんご']
print(fruits_list.count('バナナ'))
print(fruits_list)
fruits_list[4] = 'ざくろ', 'スイカ'
print(fruits_list)

print(fruits_list[4])

fruits_list.pop()
print(fruits_list)

print('###################')

fruits_list.pop(4)
print(fruits_list)

fruits_list.remove('バナナ')
print(fruits_list)

# del fruits_list
# print(fruits_list)

del fruits_list[:]
print(fruits_list)