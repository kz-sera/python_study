from decimal import Decimal as decimal

def base_body_date():
    while True:
        try:
            gender = int(input('あなたの性別を男性なら０,女性なら１と入力してください'))
            if gender != 0 and gender != 1:
                print('適切な値を入力してください')
                continue 
            break
        except:
            print('適切な値を入力してください') 

    while True:
        try:
            age = int(input('あなたの年齢を入力してください'))
            break
        except:
            print('適切な値を入力してください')
    while True:
        try:
            kg = float(input('あなたの体重を入力してください'))
            break
        except:
            print('適切な値を入力してください')

    while True:
        try:
            height = (input('あなたの身長を入力してください'))
            if '.' not in height:
                height = int(height) / 100
            elif '.' in height:
                height = float(height)
            break
        except:
            print('適切な値を入力してください')
   
    print(gender)
    print(age)
    print(kg)
    print(height)
    return gender, age, kg, height,

def BMI(kg, height):
    BMI = kg / (height ** 2)
    BMI = decimal(BMI).quantize(decimal('0.01'))
    print(BMI)

def 適正体重(height):
    適正体重 = (height ** 2) * 22
    適正体重 = decimal(適正体重).quantize(decimal('0.1'))
    print(適正体重)



def base_metabolism(gender, age, kg, height):
    height = height * 100
    if gender == 0:
        base_metabolism = 66 + 13.7 * kg + 5.0 * height - 6.8 * age
    elif gender == 1:
        base_metabolism = 665.1 + 9.6 * kg + 1.7 * height - 7.0 * age
    print(base_metabolism)




if __name__ =='__main__':
    gender, age, kg, height = base_body_date()
    BMI(kg, height)
    適正体重(height)
    base_metabolism(age=age, kg=kg, gender=gender, height=height)



#適正体重　= 身長(m)^2 * 22

#男性：66+13.7×体重kg+5.0×身長cm－6.8×年齢
#女性：665.1+9.6×体重kg+1.7×身長cm－7.0×年齢

