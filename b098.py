x = input().split()#NMTK

tweet_count = int(x[0])
observe_time = int(x[1])
time_range = int(x[2])
buzz_border = int(x[3])

good_list = []
point = 0

#発言の回数分空のlistを作成する
for i in range(tweet_count):
    good_list.append([])

#good_list にいいねの数を詰め込む
for i in range(observe_time):
    good = input().split()
    for j in range(len(good)):
        good_list[j].append(int(good[j]))

for i in range(tweet_count):
    for j in range(observe_time - time_range + 1):
        count = 0
        for k in range(time_range):
            count += good_list[i][j + k]
            if count >= buzz_border:
                print('yes' + ' ' + str(j + k + 1))
                point += 1
                # 最初にバズった時間を表示したいので break で抜ける
                break
        # 既にバズった時間を出力済みならこれ以上先の時間帯を調べる必要はないので break で抜ける
        if point > 0: break
    if point == 0:
        print('no 0')
    else:
        # 初期化する
        point = 0