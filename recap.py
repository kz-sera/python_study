#[2018/09/22] 変数の宿題
#1. first_name変数に自分の名前を代入してください
#2. last_name変数に自分の苗字を代入してください
#3. age変数に自分の年齢を代入してください
#4. over_好きな数字の変数を作り、自分の年齢がその数字より上ならTrueを、下ならFalseを代入してください
#5. 所持金変数を作り好きな金額を代入してください
#6. 賭け金を聞いて入力を受け付ける変数を作ってください
#7. ユーザーが入力した数値を所持金から引いた数を"残金: 数字"と出力してください
# print('####################################')
# #1
# first_name = 'kazui'
# print(first_name)
# #2
# last_name = 'sera'
# print(last_name)
# #3
# age = 43
# print(age)
# #4
# over_4 = False
# print(over_4)
# #5
# money = 4300
# print('所持金：', money)
# #6
# bit = int(input('掛け金を入力してください'))
# print('掛け金:', bit)
# #7
# money -= bit
# print('所持金：', money)





#[2018/09/23] リストの宿題
#1. 以下の条件にあうリストを作れ
#   ・友達を最低5人含めたfriendsリスト
#   ・果物を列挙したfruitsリスト。そのうち３つは必ず重複すること。重複の数は任せる
#   ・好きなゲームを列挙したgamesリスト
#   ・なんでも入れられる空のanythingリスト
#2. friendsリストの2番目の要素を表示しろ
#3. fruitsリストの5番目の要素を表示しろ
#4. gamesリストのindex番号6を表示しろ
#5. 上記2~4で表示した要素をanythingリストに追加してanythingリストを表示しろc
#6. +=の追加方法を使って、好きな名前をひらがな1文字ずつ格納しているリストを作れ
#7. fruitsリストの重複している要素が何個重複しているかを表示しろ
#8. friendsリストの要素数を表示しろ
#9. friendsリストのインデックス5番の要素を別の要素に上書きしろ
#10.pop()を使って好きなリストの好きな要素を削除し、削除した後のリストを表示しろ
#11.remove()を使って好きなリストの好きな要素を削除し、削除した後のリストを表示しろ
#12. delを使って4つのリスト全てを空にしろ
# print('####################################')

# #1
# friends_list = ['はやと', 'はるひろ', 'たくみ', 'ジョシュワ', 'さちこ']
# print(friends_list)

# fruits_list = ['りんご', 'スイカ', 'バナナ', 'ブドウ', 'バナナ', 'レモン', 'バナナ', '柿']
# print(fruits_list)

# games_list = ['ボーダーランズ２', 'ドラゴンズドグマ', '大神', 'スカイリム', 'ダークソウル３', 'ブラッドボーン', '.hack//G.U.', 'デビルメイクライ']
# print(games_list)

# anything_list = []
# print(anything_list)

# #2
# print(friends_list[1])

# #3
# print(fruits_list[4])

# #4
# print(games_list[6])

# #5
# anything_list.append('はるひろ')
# anything_list.append('バナナ')
# anything_list.append('.hack//G.U.') #これだとタプルが入ってしまう。個別に入れるようにappend()してください -by.J
# print(anything_list)

# #6
# yuuri_name = []
# yuuri_name += 'せらゆうり'
# print(yuuri_name)

# #7
# print(fruits_list.count('バナナ'))

# #8
# len_list = len(friends_list)
# print(len_list)

# #9
# friends_list[4] = 'なお'
# print(friends_list)

# #10
# fruits_list.pop(1)
# print(fruits_list)

# #11
# games_list.remove('大神')
# print(games_list)

# #12
# del friends_list[:], fruits_list[:], games_list[:], anything_list[:]
# print(friends_list, fruits_list, games_list, anything_list) #やり方は合ってますが削除が3つのみです。anything_listも削除してください -by.J






#[2018/09/29] if構文の宿題
#1. 性別を保存するgender変数を定義して性別を文字列(string)型として代入せよ。
#   その性別が男性なら「私は男性です」、女性なら「私は女性です」とプリントをするようなif文を作れ
#   その際、elseは使わないようにせよ
gender = ('male')
if gender == 'male':
    print('私は男性です')
elif gender == 'female':
    print('私は女性です')
#2. 気温を示すtemperature変数を宣言して現在の気温を小数点第一まで代入せよ
#   その気温が25℃を超えていれば「今日は暑いです」、18~24℃なら「快適な気温です」、15~17℃なら「肌寒いです」、
#   その他は「寒いです」と表示するif文を作れ。なお、18~24, 15~17は範囲指定で表現せよ。
temperature = int(input('現在の気温を入力してください'))
if 25 <= temperature:
    print('今日は暑いです')
elif 18 <= temperature <= 24:
    print('快適な温度です')
elif 15 <= temperature <= 17:
    print('肌寒いです')
else:
    print('今日は寒いです')
#3. 文字列を代入する変数を宣言し、好きな文字列を代入せよ。
#   その文字列に特定の文字が含まれているかをif文を使って検索し、もし入っていれば「○◯は入っている」というように表示し、
#   入っていないなら「○◯は入っていない」と表示するif文を作成せよ
name = 'komiyama mika'
if 'm' in name:
    print('mは名前の中に入っています')
elif 's' not in name:
    print('sは名前の中に入っていません')
print('####################################')





#[2018/10/02] for構文の宿題
#1. for文で使うためのリスト(好きなもの)を2つ作れ
fruits_list = ['りんご', 'れもん', 'ブドウ', 'メロン', 'バナナ', 'みかん', 'キウイ', 'スイカ']
friends_list = ['はやと', 'はるひろ', 'たくみ', 'ジョシュワ', 'さちこ', 'つねひさ', 'ひろき', 'なお']
#2. そのリスト2つをfor文を使ってそれぞれのリストの要素を表示せよ
for fruits in fruits_list:
    print(fruits)
for friends in friends_list:
    print(friends)
#3. ネットでrange関数について調べ、その関数を用いて自分の名前を10回表示せよ
#   検索例)python range, python for
for n in range(10):
    print('kazui')
print('####################################')





#[2018/10/02] 関数の宿題
#1. 自分の名前を表示するmy_name関数を宣言して実行せよ
def my_name():
    print('かずい')
my_name()
#2. 引数を1つもつsay_anything関数を宣言し、関数に好きなことを言わせろ(definition.pyの#引数の項目を参照)
def say_anything(a):
    print('hello, {a}'.format(a = a))
say_anything('maguro')
#3. 引数を2つもつfull_name関数を宣言せよ。この関数は2つの引数の文字列を連結し表示する。その際、苗字と名前の間のスペースに気をつけろ.
def full_name(first_name, last_name):
    full_name = first_name + '' + last_name
    return full_name
full_name = full_name(last_name = ' sera', first_name = 'kazui')
print(full_name)




#[2018/10/05] BMI計算
#作ったBMIプログラムで、ユーザーのBMI値によって「痩せすぎ」「普通」「肥満」を判定するプログラムを追記せよ。
#この時、追記はbody_calculate.pyに行え