from decimal import Decimal as decimal


def base_body_data():
    while True:
        try:
            print('性別を入力してください')
            gender = int(input('[0. 男性   1. 女性]'))
            if gender != 0 and gender != 1:
                print('適切な値を入力してください')
                continue
            break
        except:
            print('適切な値を入力してください')

    while True:
        try:
            age = int(input('年齢を入力してください'))
            break
        except:
            print('適切な値を入力してください')

    while  True:
        try:
            weight = float(input('体重を入力してください'))
            break
        except:
            print('適切な値を入力してください')

    while True:
        try:
            height = input('身長を入力してください')
            if "." not in height:
                height = int(height) / 100
            elif '.' in height:
                height = float(height)
            break
        except:
            print('適切な値を入力してください')
            
    if gender == 0:
        print('性別: 男性')
    elif gender == 1:
        print('性別: 女性')
    print('年齢: {age}歳'.format(age=age))
    print('体重: {weight}kg'.format(weight=weight))
    print('身長: {height}m'.format(height=height))
    return gender, age, weight, height


def BMI(weight, height):
    bmi = weight / (height ** 2)
    bmi = decimal(bmi).quantize(decimal('0.01'))
    print('BMI: {bmi}'.format(bmi=bmi))


def suitable_weight(weight, height):
    suitable_weight = (height ** 2) * 22
    suitable_weight = decimal(suitable_weight).quantize(decimal('0.01'))
    print('適正体重: {suitable_weight}kg'.format(suitable_weight=suitable_weight))
    print('適正体重より: +{over_weight}'.format(over_weight=decimal(weight) - suitable_weight))


def basa_metabolism(gender, age, weight, height):
    height = height * 100
    #男性：66+13.7×体重kg+5.0×身長cm－6.8×年齢
    #女性：665.1+9.6×体重kg+1.7×身長cm－7.0×年齢
    if gender == 0:
        base_meta = 66 + 13.7 * weight + 5.0 * height - 6.8 * age
    elif gender == 1:
        base_meta = 665.1 + 9.6 * weight + 1.7 * height - 7.0 * age
    print('基礎代謝: {bs}kcal'.format(bs=base_meta))






if __name__ == '__main__':
    gender, age, weight, height = base_body_data()
    BMI(weight, height)
    suitable_weight(weight=weight, height=height)
    basa_metabolism(gender, age, weight, height)