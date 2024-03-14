z = input().split()

#カードの枚数
cards_count = int(z[0])

#グループの枚数
count_per_set = int(z[1])

#シャッフルの回数
shuffle_count = int(z[2])

#カードの内訳
def create_card_list(n):
    lst = []
    for i in range(1,n+1):
        lst.append(i)
    return(lst)

def create_card_set(cards, size):
    card_set = []
    for start in range(0, len(cards), size):
        card_set.append(cards[start:start + size])
    return(card_set)

def creat_musan(card_set):
    musan = []
    for cards in card_set:
        for card in cards:
            musan.append(card)
    return(musan)

#グループの枚数ごとにグループ化
#最大がgroup_cards
card_set = create_card_set(create_card_list(cards_count), count_per_set)

for _ in range(shuffle_count):
    card_set.reverse()
    card_set = creat_musan(card_set)
    card_set = create_card_set(card_set, count_per_set)

for card in creat_musan(card_set):
    print(card)