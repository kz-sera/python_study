#BMI = 体重(kg) / 身長(m)^2

from decimal import Decimal as decimal

kg = float(input('あなたの体重を入力してください'))
height = (input('あなたの身長を入力してください'))
if '.' not in height:
    height = int(height) / 100
elif '.' in height:
    height = float(height)
print(kg)
print(height)

BMI = kg / (height ** 2)
BMI = decimal(BMI).quantize(decimal('0.01'))
print(BMI)

BMI_round = round(BMI, 2)
print(BMI_round)