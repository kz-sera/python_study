#whaile文の勉強
count = 0
while count < 10:
    count += 1
    print(count)
    if count == 8:
        break
    elif count == 5:
        continue
    print('while文')
else:
    print('while文終了')