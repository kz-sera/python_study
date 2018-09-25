
import random as rand
#所持金

#キーボード入力の受付

#トランプカード(A~K)のリスト

#トランプカードをランダムで選出するランダム変数

#プレイヤーの手を格納する空のリスト

money = 3000
print('所持金', money)

bit = int(input('掛け金を入力してください'))
print('掛け金', bit)

trump_card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
print(trump_card)

trump_rand =rand.randint(0, len(trump_card)-1)
print(trump_card[trump_rand])

player_hand = []
print(player_hand)