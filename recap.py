#[2018/09/22] 変数の宿題
#1. first_name変数に自分の名前を代入してください
#2. last_name変数に自分の苗字を代入してください
#3. age変数に自分の年齢を代入してください
#4. over_好きな数字の変数を作り、自分の年齢がその数字より上ならTrueを、下ならFalseを代入してください
#5. 所持金変数を作り好きな金額を代入してください
#6. 賭け金を聞いて入力を受け付ける変数を作ってください
#7. ユーザーが入力した数値を所持金から引いた数を"残金: 数字"と出力してください

#1
first_name = 'kazui'
print(first_name)
#2
last_name = 'sera'
print(last_name)
#3
age = 43
print(age)
#4
over_4 = False
print(over_4)
#5
money = 4300
print('所持金：', money)
#6
bit = int(input('掛け金を入力してください'))
print('掛け金:', bit)
#7
money -= bit
print('所持金：', money)